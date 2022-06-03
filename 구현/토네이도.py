n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

out = 0
# 왼 아 오 위
dx = [0,1,0,-1]
dy = [-1,0,1,0]

x=y=n//2

d=2
distD = 0
while True:
    d = (d+1)%4
    distD +=1
    dist = distD//2
    if dist == 0:
        board[x][y]=1
    for i in range(dist):
        x +=dx[d]
        y +=dy[d]    
        board[x][y]=1
        if x == 0 and y==0:
            break
    for b in board:
        print(*b)
    print('----')
   