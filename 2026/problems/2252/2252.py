import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
adj = [[] for _ in range(n+1)]
deg = [0] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
    deg[b] += 1

q = deque()
for i in range(1, n+1):
    if deg[i] == 0:
        q.append(i)
result = []
while q:
    cur = q.popleft()
    result.append(cur)
    for nxt in adj[cur]:
        deg[nxt] -= 1
        if deg[nxt] == 0:
            q.append(nxt)

print(" ".join(map(str, result)))