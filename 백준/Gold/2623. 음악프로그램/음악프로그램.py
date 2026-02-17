from collections import deque
import sys
input = sys.stdin.readline


n,m = map(int,input().split())
adj = [[] for _ in range(n+1)]
deg = [0] * (n+1)
visited = [False] * (n+1)
for _ in range(m):
    orders = list(map(int,input().split()))
    for i in range(len(orders)-1, 1, -1):
        cur, nxt = orders[i], orders[i-1]
        adj[cur].append(nxt)
        deg[nxt] += 1

q = deque()

for i in range(1,len(deg)):
    if deg[i] == 0:
        q.append(i)
# print(deg)
ans = []
while q:
    cur = q.popleft()
    visited[cur] = True
    ans.append(cur)

    for nxt in adj[cur]:
        # print(nxt)
        deg[nxt] -= 1
        if deg[nxt] == 0:
            q.append(nxt)

all_visited = all(x for x in visited[1:])
if not all_visited:
    print(0)
else:
    for i in ans[::-1]:
        print(i)