import sys
sys.setrecursionlimit(10_000)
input = sys.stdin.readline

# 크루스칼 알고리즘
v, e = map(int, input().split())

edges = []

for _ in range(e):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

p = [-1] * (v+1)

def find(x):
    if p[x] < 0:
        return x
    p[x] = find(p[x])
    return p[x]

def union(u,v):
    u = find(u)
    v = find(v)
    if u == v:
        return False
    p[u] = v
    return True

edges.sort()
cnt = 0
result = 0
for cost, a, b in edges:
    a = find(a)
    b = find(b)
    ## 같은 그룹이면
    if a == b:
        continue
    union(a,b)
    cnt += 1
    result += cost
    if cnt == e-1:
        break
print(result)


