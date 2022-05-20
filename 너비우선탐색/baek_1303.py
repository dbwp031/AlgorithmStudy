from collections import deque

n,m = map(int,input().split())
board = []
for _ in range(m):
    board.append(list(input()))
wp = 0
bp = 0

visited = [[False]*n for _ in range(m)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
que = deque([])
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            que.append([i,j])
            visited[i][j]=True
            cnt = 1
            while que:
                x,y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0<=nx<=m-1 and 0<=ny<=n-1 and not visited[nx][ny] and board[nx][ny]==board[i][j]:
                        que.append([nx,ny])
                        cnt+=1
                        visited[nx][ny]=True
            if board[x][y]=='W':
                wp += cnt**2
            else:
                bp += cnt**2
print(wp,bp)