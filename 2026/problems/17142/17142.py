import copy
import itertools
import collections

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

dx = (0,1,0,-1)
dy = (1,0,-1,0)

EMPTY = 0
WALL = 1
VIRUS = 2

viruses = []
for i in range(N):
    for j in range(N):
        if board[i][j] == VIRUS:
            viruses.append((i,j))

active = copy.deepcopy(board)
for i in range(N):
    for j in range(N):
        if active[i][j] == EMPTY:
            active[i][j] = -1
        elif active[i][j] == WALL:
            active[i][j] = -2
EMPTY = -1
WALL = -2

min_cost = 1e9
for tvirus in itertools.combinations(viruses, M):
    board = copy.deepcopy(active)
    for (i,j) in viruses:
        board[i][j] = EMPTY
    for (i,j) in tvirus:
        board[i][j] = 0
    
    que = collections.deque()
    for (ti, tj) in tvirus:
        que.append((ti,tj, 0))

    tvcost = 0
    while que:
        x,y,cost = que.popleft()
        tvcost = max(tvcost, cost)
        breakFlag = False
        for di in range(4):
            nx = x + dx[di]
            ny = y + dy[di]
            if 0<=nx<N and 0<=ny<N and board[nx][ny] == EMPTY:
                if cost + 1 > min_cost:
                    breakFlag = True

                board[nx][ny] = cost + 1
                que.append((nx,ny,cost + 1))
        if breakFlag:
            break
    print(tvcost)
    for b in board:
        print(b)
    min_cost = min(min_cost, tvcost)
print(min_cost)
