import sys
import copy
input = sys.stdin.readline
OUTSIDE = 1
HOLE = 2
CHEESE = 3
NOT_DEFINED = 4
WILL_MELT = 5
nx = [-1,0,1,0]
ny = [0,1,0,-1]
row, col = map(int,input().split())
board = []
for _ in range(row):
    board.append(list(map(int, input().split())))
air_board = copy.deepcopy(board)
def 녹아야될_치즈_찾기():
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                for k in range(4):
                    tx = i + nx[k]
                    ty = j + ny[k]
                    if 0<=tx<row and 0<=ty<col and air_board[tx][ty] == OUTSIDE:
                        air_board[i][j] = WILL_MELT

def 구멍인지_바깥인지_확인하기():
    # 어떻게?
    # 가장자리와 연결될 수 있다면 바깥
    # 가장자리와 연결되지 못한다면 구멍
    visited = [[False for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            air_board[i][j] = CHEESE if board[i][j] == 1 else NOT_DEFINED
    
    que = [(0,0)]
    visited[0][0] = True
    air_board[0][0] = OUTSIDE
    
    while(len(que)!= 0):
        now_r, now_c = que.pop(0)
        air_board[now_r][now_c] = OUTSIDE
        
        for i in range(4):
            tx = now_r + nx[i]
            ty = now_c + ny[i]
            if 0<=tx<row and 0<=ty<col and board[tx][ty] != 1 and not visited[tx][ty]:
                visited[tx][ty] = True
                que.append((tx,ty))
    for i in range(row):
        for j in range(col):
            if air_board[i][j] == NOT_DEFINED:
                air_board[i][j] = HOLE
            
    
def 녹이기():
    for i in range(row):
        for j in range(col):
            if air_board[i][j] == WILL_MELT:
                board[i][j] = 0
def 모두_녹았나_확인():
    all_melt_flag = True
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1: 
                all_melt_flag = False
                break
    return all_melt_flag
def 치즈_개수_구하기():
    cheese_count = 0
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1: 
                cheese_count+=1
    return cheese_count
    
def 한시간_프로세스():
    구멍인지_바깥인지_확인하기()
    녹아야될_치즈_찾기()
    녹이기()
hour = 0
while(True):
    cheese_count = 치즈_개수_구하기()
    한시간_프로세스()
    hour +=1
    if(모두_녹았나_확인()):
        print(hour)
        print(cheese_count)
        break
