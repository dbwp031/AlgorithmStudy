from collections import deque
r,c=map(int,input().split())
board = []
for _ in range(r):
    board.append(list(input()))

ice = deque([])

dx=[-1,0,1,0]
dy=[0,1,0,-1]
visited = [[False]*c for _ in range(r)]
dovi = []
for x in range(r):
    for y in range(c):
        if board[x][y]=='L':
            dovi.append([x,y])
            continue
        if board[x][y]=='X' and not visited[x][y]:
            visited[x][y]=True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<=r-1 and 0<=ny<=c-1 and board[nx][ny]!='X':
                    ice.append([x,y,0])
                    break
INF = 1e9
parent = [['.']*c for _ in range(r)]
visited = [[False]*c for _ in range(r)]
dque = deque([])
for i in range(2):
    dque.append([dovi[i][0],dovi[i][1],i])

while dque:
    x,y,idx = dque.popleft()
    parent[x][y]=idx
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<=r-1 and 0<=ny<=c-1 and board[nx][ny]!='X' and not visited[nx][ny]:
            dque.append([nx,ny,idx])
            visited[nx][ny]=True
                

visited = [[False]*c for _ in range(r)]
continueDay = True
while ice and continueDay:
    mold_t = len(ice)
    for _ in range(mold_t):
        ix,iy,day = ice.popleft()
        # print(day)
        board[ix][iy]='.'

        dov0 = False
        dov1 = False

        for i in range(4):
            nx = ix + dx[i]
            ny = iy + dy[i]
            if 0<=nx<=r-1 and 0<=ny<=c-1:
                if parent[nx][ny]==0:
                    dov0=True
                elif parent[nx][ny]==1:
                    dov1=True
        if dov0 and dov1:
            result = day
            continueDay=False
        elif dov0:
            parent[ix][iy]=0
        elif dov1:
            parent[ix][iy]=1
                

        for i in range(4):
            nix = ix + dx[i]
            niy = iy + dy[i]
            if 0<=nix<=r-1 and 0<=niy<=c-1 and board[nix][niy]=='X' and not visited[nix][niy]:
                ice.append([nix,niy,day+1])
                visited[nix][niy]=True

    # for b in parent:
    #     print(*b)
if continueDay==False:
    print(0)
else:
    print(day+1)