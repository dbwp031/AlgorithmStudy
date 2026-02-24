import sys
input = sys.stdin.readline

n = int(input())
costs = [list(map(int,input().split())) for _ in range(n)]

prev = costs[0]
# dp[i][j] = i번째 집에 j색을 선택했을 때의 최솟값
for i in range(1,n):
    cur = [0] * 3
    for j in range(3):
        cur[j] = min(prev[(j+1)%3], prev[(j+2)%3]) + costs[i][j]
    prev = cur
# for d in dp[:n]:
#     print(d)
print(min(cur))