import sys
import heapq

sys.setrecursionlimit(10_000)
input = sys.stdin.readline


# # 크루스칼 알고리즘
# v, e = map(int, input().split())
# edges = []

# for _ in range(e):
#     a,b,c = map(int, input().split())
#     edges.append((c,a,b))

# p = [-1] * (v+1)

# def find(x):
#     if p[x] < 0:
#         return x
#     p[x] = find(p[x])
#     return p[x]

# def union(u,v):
#     u = find(u)
#     v = find(v)
#     if u == v:
#         return False
#     p[u] = v
#     return True

# edges.sort()
# cnt = 0
# result = 0
# for cost, a, b in edges:
#     a = find(a)
#     b = find(b)
#     ## 같은 그룹이면
#     if a == b:
#         continue
#     union(a,b)
#     cnt += 1
#     result += cost
#     if cnt == e-1:
#         break
# print(result)

# 프림 알고리즘
v, e = map(int, input().split())

edges = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    edges[a].append((b,c))
    edges[b].append((a,c))

visited = [False] * (v+1)
heap = []
result = 0
cnt = 0

start = 1
visited[start] = True
for next_node, cost in edges[start]:
    heapq.heappush(heap, (cost, next_node))

while heap:
    cost, node = heapq.heappop(heap)
    if visited[node]:
        continue

    visited[node] = True
    result += cost
    cnt += 1

    if cnt == v-1:
        break

    for next_node, next_cost in edges[node]:
        if not visited[next_node]:
            heapq.heappush(heap, (next_cost, next_node))

print(result)    