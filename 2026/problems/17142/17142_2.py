import itertools
import collections

N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

viruses = []
empty_cnt = 0
for i in range(N):
    for j in range(N):
        if a[i][j] == 2:
            viruses.append((i,j))
        elif a[i][j] == 0:
            empty_cnt += 1

if empty_cnt == 0:
    print(0)
    exit()

INF = 10**9
ans = INF

for chosen in itertools.combinations(viruses, M):
    dist = [[-1]*N for _ in range(N)]
    q = collections.deque()

    for x, y in chosen:
        dist[x][y] = 0
        q.append((x,y))

    infected = 0
    last_time = 0

    while q:
        x, y = q.popleft()
        t = dist[x][y]

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not (0<=nx<N and 0<=ny<N):
                continue
            if a[nx][ny] == 1:
                continue
            if dist[nx][ny] != -1:
                continue
            
            dist[nx][ny] = t + 1
            q.append((nx,ny))

            if a[nx][ny] == 0:
                infected += 1
                last_time = t + 1
    
    if infected == empty_cnt:
        ans = min(ans, last_time)

print(-1 if ans == INF else ans)