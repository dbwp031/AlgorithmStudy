import sys
input = sys.stdin.readline
INF = sys.maxsize // 2

n = int(input())
m = int(input())

dist = [[INF]*(n+1) for _ in range(n+1)]
next_node = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a,b,w = map(int,input().split())
    if w < dist[a][b]:
        dist[a][b] = w
        next_node[a][b] = b # 직행 간선

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                next_node[i][j] = next_node[i][k]

# 출력 1
for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j] == INF:
            print("0", end=" ")
        else:
            print(dist[i][j], end=" ")
    print()

def get_path(start, end):
    if next_node[start][end] == 0:
        return []
    path = [start]
    while start != end:
        start = next_node[start][end]
        path.append(start)
    return path

for i in range(1,n+1):
    for j in range(1,n+1):
        path = get_path(i,j)
        if not path:
            print(0)
        else:
            print(len(path), *path)