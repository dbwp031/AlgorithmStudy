import sys
sys.setrecursionlimit(10_000)

n,m = map(int,input().split())

p = [-1] * (n+1)

# def find(x):
#     if p[x] < 0:
#         return x
#     p[x] = find(p[x])
#     return p[x]

def find(x):
    root = x
    while p[root] >= 0:
        root = p[root]
        
    while x != root:
        p[x], x = root, p[x]
    return root

def union(u,v):
    u = find(u)
    v = find(v)
    if u == v :
        return False
    p[u] = v
    return True

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a,b)
    elif op == 1:
        ag = find(a)
        bg = find(b)
        if ag == bg:
            print("YES")
        else:
            print("NO")