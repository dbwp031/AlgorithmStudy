n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
moves = []
for _ in range(m):
    a,b = map(int,input().split())
    a-=1
    moves.append([a,b])
#     왼 왼위 위 위오 오
dx = [0, -1,-1, -1,0,1,1, 1]
dy = [-1,-1, 0, 1, 1,1,0,-1]
# 왼위 왼아 오위 오아
gx = [-1,+1,-1,+1]
gy = [-1,-1,+1,+1]

clouds = [[n-2,0],[n-2,1],[n-1,0],[n-1,1]]

for move in moves:
    visited = [[False]*n for _ in range(n)]
    d,cnt = move
    for _ in range(cnt):
        for i in range(len(clouds)):
            clouds[i][0] = (clouds[i][0]+dx[d]) % n
            clouds[i][1] = (clouds[i][1]+dy[d]) % n
    
    for cloud in clouds:
        x,y=cloud
        visited[x][y]=True
        board[x][y]+=1
    for cloud in clouds:
        x,y= cloud
        for g in range(4):
            nx = x + gx[g]
            ny = y + gy[g]
            if 0<=nx<=n-1 and 0<=ny<=n-1 and board[nx][ny] != 0:
                board[x][y]+=1
    new_clouds = []
    for x in range(n):
        for y in range(n):
            if board[x][y] >=2 and not visited[x][y]:
                board[x][y]-=2
                new_clouds.append([x,y])
    clouds = new_clouds
answer = 0
for x in range(n):
    for y in range(n):
        answer +=board[x][y]

print(answer)