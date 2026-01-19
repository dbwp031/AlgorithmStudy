import sys
input = sys.stdin.readline

DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

N, M = map(int,input().split())
r,c,d = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

dr = [-1,0,1,0]
dc = [0,1,0,-1]

NOT_CLEANED = 0
WALL = 1
CLEANED = 2



def clean_and_move():
    global board, r, c, d, N, M
    answer = 0
    while(True):
        if board[r][c] == NOT_CLEANED:
            board[r][c] = CLEANED
            answer += 1

        side_all_cleaned = True
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M and board[nr][nc] == NOT_CLEANED:
                side_all_cleaned = False
        
        move_back = True
        if side_all_cleaned:
            nd = (d + 2) % 4 # 후진
            nr = r + dr[nd]
            nc = c + dc[nd]
            if 0<=nr<N and 0<=nc<M and board[nr][nc] == WALL:
                move_back = False

            if move_back:
                r,c = nr,nc
                continue
            else:
                break
        
        if not side_all_cleaned:
            for i in range(4):
                d = (d-1)%4
                nr = r + dr[d]
                nc = c + dc[d]
                if 0<=nr<N and 0<=nc<M and board[nr][nc] == NOT_CLEANED:
                    r,c = nr,nc
                    break
    print(answer)
clean_and_move()