import sys
import copy
input = sys.stdin.readline

a,b,c = map(int,input().split())
max_water = [a,b,c]
visited = [[[False]*(c+1) for _ in range(b+1)] for _ in range(a+1)]

q = []
q.append([0,0,c])
visited[0][0][c] = True

def pour(before, x,y):
    if x == y: return  before
    if before[x] + before[y] <= max_water[y]:
        before[y] = before[x]+before[y]
        before[x] = 0
    else:
        before[x] = before[x]-(max_water[y]-before[y])
        before[y] = max_water[y]
    return before
while q:
    before = q.pop(0)
    for i in range(3):
        for j in range(3):
            if i == j: continue
            aa,ab,ac = pour(copy.deepcopy(before),i,j)
            if not visited[aa][ab][ac]:
                visited[aa][ab][ac] = True
                q.append([aa,ab,ac])
answer = []

for i in range(b+1):
    for j in range(c+1):
        if visited[0][i][j]: answer.append(j)
answer.sort()
print(" ".join(map(str, answer)))
