from collections import deque
# m: 가로 n:세로 h: 높이
m,n,h = map(int,input().split())
board = []
# 위 왼쪽 아래 오른쪽 하늘 땅
# 보드0번재가 가장 위쪽 판인가? 아래쪽 판인가?
# 일단 0번쨰가 땅, h번째가 하늘
dx = [-1,0,1,0,0,0]
dy = [0,-1,0,1,0,0]
dz = [0,0,0,0,1,-1]

for _ in range(h):
    temp = []   
    for _ in range(n):
        temp.append(list(map(int,input().split())))
    board.append(temp)

que = deque([])

visited = [[[False]*m for _ in range(n)] for _ in range(h)]
for z in range(h):
    for x in range(n):
        for y in range(m):
            if board[z][x][y]==1:
                que.append([z,x,y,0])
                visited[z][x][y]=True
while que:
    z,x,y,time = que.popleft()
    for d in range(6):
        nz = z + dz[d]
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nz<=h-1 and 0<=nx<=n-1 and 0<=ny<=m-1 and visited[nz][nx][ny]==False and board[nz][nx][ny]==0:
            visited[nz][nx][ny] = True
            board[nz][nx][ny]=1
            que.append([nz,nx,ny,time+1])
allGood = True
for z in range(h):
    for x in range(n):
        for y in range(m):
            if board[z][x][y]==0:
                allGood=False
if allGood:
    print(time)
else:       
    print(-1)