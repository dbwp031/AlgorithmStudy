n,m,k = map(int,input().split())
board = [[[] for _ in range(n)]for _ in range(n)]

for _ in range(m):
    r,c,_m,s,d = map(int,input().split())
    r-=1
    c-=1
    board[r][c].append([_m,s,d])
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def move(board):
    new_board = [[[] for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for g in range(len(board[i][j])):
                _m,s,d = board[i][j][g]
                x = (i + dx[d]*s) % n
                y = (j + dy[d]*s) % n
                new_board[x][y].append([_m,s,d])
    return new_board

def merge(board):
    allS = [0,2,4,6]
    allD = [1,3,5,7]
    new_board = [[[] for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mess = 0
            speed = 0
            allOdd = True
            allEven = True
            if len(board[i][j])>=2:
                for h in range(len(board[i][j])):
                    _m,s,d = board[i][j][h]
                    mess+=_m
                    speed+=s
                    if d % 2 == 0: allOdd = False
                    else: allEven = False
                mess = mess // 5
                speed = speed // len(board[i][j])
                if mess!=0:
                    if allOdd or allEven:
                        for g in range(4):
                            new_board[i][j].append([mess,speed,allS[g]])
                    else:
                        for g in range(4):
                            new_board[i][j].append([mess,speed,allD[g]])
            else:
                new_board[i][j]=board[i][j]
    return new_board

for _ in range(k):
    board = merge(move(board))
ans= 0

for i in range(n):
    for j in range(n):
        for g in range(len(board[i][j])):
                ans+=board[i][j][g][0]
print(ans)