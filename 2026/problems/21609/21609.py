import sys
import collections

input = sys.stdin.readline

N,M = map(int,input().split())
EMPTY = -2
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

class Group:
    def __init__(self, group):
        self.group = group
        self.count = len(group)
        self.raincount = 0
        
        rpgroup = []
        for gx,gy in group:
            if board[gx][gy] == 0:
                self.raincount += 1
            else:
                rpgroup.append((gx,gy))
        
        self.rprow = max(r for r,c in rpgroup)        
        self.rpcol = max(c for r,c in rpgroup if r == self.rprow)

    # a.__lt__(b) => a is less than b    
    def __lt__(self, other):
        if self.count != other.count:
            return self.count < other.count
        if self.raincount != other.raincount:
            return self.raincount < other.raincount
        if self.rprow != other.rprow:
            return self.rprow < other.rprow
        return self.rpcol < other.rpcol

    def __repr__(self):
        return (
            f"Group(count={self.count}, "
            f"rain={self.raincount}, "
            f"rprow={self.rprow}, "
            f"rpcol={self.rpcol})"
        )

def find_maxblock_and_delete(board):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == -1 or board[i][j] == 0 or board[i][j] == EMPTY:
                continue
            if visited[i][j] != 0:
                continue

            deq = collections.deque()
            deq.append((i,j))
            visited[i][j] = len(groups) + 1
            group = [(i,j)]
            gi = len(groups) + 1
            tnum = board[i][j]
            while deq:
                x,y = deq.pop()
                for di in range(4):
                    nx = x + dx[di]
                    ny = y + dy[di]
                    if 0<=nx<N and 0<=ny<N and ((visited[nx][ny] == 0 and board[nx][ny] == tnum) or (visited[nx][ny] != gi and board[nx][ny] == 0)):
                        deq.append((nx,ny))
                        visited[nx][ny] = gi
                        group.append((nx,ny))
            groups.append(group)
    
    fgroups = []
    for g in groups:
        if len(g) > 1:
            fgroups.append(Group(g))
    cont = True
    if len(fgroups) == 0:
        cont = False
        return cont, 0, board
        
    mgroup = max(fgroups)
    # print(mgroup.group)
    
    score = mgroup.count ** 2
    for gx, gy in mgroup.group:
        board[gx][gy] = EMPTY
    return cont, score, board
    # for g in fgroups:
    #     print(g)

def gravity(board, empty=-2, wall=-1):
    n = len(board)
    for c in range(n):
        write = n - 1 # 블록이 떨어질 위치 (아래에서부터 채움)
        for r in range(n-1, -1, -1):
            if board[r][c] == wall:
                # 벽을 만나면 벽은 고정, 그 위 구간은 write를 벽 위로 리셋
                write = r-1
            elif board[r][c] != empty:
                # 블록이면 write 위치로 내린다(필요시 스왑/이동)
                val = board[r][c]
                if write != r:
                    board[r][c] = empty
                    board[write][c] = val
                write -= 1
    return board

def rotate_90_left(a):
  # (i, j) -> (N-1-j, i)
  # 1. 전치 (i, j) -> (j, i)
  # 2. 열 뒤집기 (j, i) -> (N-1-j, i)
  # 코드 상에는 열 뒤집기 -> 전치 순서로 구현됨
    return [list(row) for row in zip(*a)][::-1]

cont = True
answer = 0
while cont:
    cont, score, board = find_maxblock_and_delete(board)
    if not cont:
        break
    answer += score
    board = gravity(board)
    board = rotate_90_left(board)
    board = gravity(board)

print(answer)    
