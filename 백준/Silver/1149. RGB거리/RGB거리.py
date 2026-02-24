import sys
input = sys.stdin.readline

n = int(input())
costs = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(1_000)]
dp[0] = costs[0]
# dp[i][j] = i번째 집에 j색을 선택했을 때의 최솟값
for i in range(1,n):
    for j in range(3):
        dp[i][j] = min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + costs[i][j]
# for d in dp[:n]:
#     print(d)
print(min(dp[n-1]))