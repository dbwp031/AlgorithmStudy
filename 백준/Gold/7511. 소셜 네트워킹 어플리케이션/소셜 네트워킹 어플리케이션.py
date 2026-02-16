import sys
sys.setrecursionlimit(10_000)
input = sys.stdin.readline

t = int(input())


for i in range(1, t+1):
    print(f"Scenario {i}:")
    n = int(input())
    k = int(input())
    p = [-1] * (n+1)
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

    for _ in range(k):
        a,b = map(int,input().split())
        union(a,b)
    m = int(input())
    for _ in range(m):
        u,v = map(int,input().split())
        ug = find(u)
        vg = find(v)
        if ug == vg:
            print("1")
        else:
            print("0")
    print()
