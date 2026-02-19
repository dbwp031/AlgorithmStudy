from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
costs = [-1] * (n+1)
adj = [[] for _ in range(n+1)]
deg = [0] * (n+1)

for i in range(1,n+1):
    inps = list(map(int, input().split()))
    cost = inps[0]
    costs[i] = cost
    for j in range(1, len(inps)):
        node = inps[j]
        if node == -1:
            break
        adj[node].append(i)
        deg[i] += 1

# 각각을 짓는 데에 걸리는 최단 시간을 구하고 그것의 max값을 구하면 된다.
dp = [-1] *(n+1)
q = deque()
for i in range(1, len(deg)):
    if deg[i] == 0:
        q.append(i)
        dp[i] = costs[i]

while q:
    cur = q.popleft()
    for nxt in adj[cur]:
        deg[nxt] -= 1
        dp[nxt] = max(dp[nxt], dp[cur] + costs[nxt])
        if deg[nxt] == 0:
            q.append(nxt)

for node in dp[1:]:
    print(node)
    