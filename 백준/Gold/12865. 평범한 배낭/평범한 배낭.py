import sys
input = sys.stdin.readline

n,k = map(int,input().split())
ws = []
vs = []
for _ in range(n):
    w,v = map(int,input().split())
    ws.append(w)
    vs.append(v)
# i번째를 선택할지, 고려할지를 결정해야함.
# 고려가 맞음.

dp = [[0]*100_001 for _ in range(100)]

for i in range(ws[0], k+1):
    dp[0][i] = vs[0]

for i in range(1, n):
    w,v = ws[i], vs[i]
    # dp[i][j] = i번째 원소까지 고려했을 때, j무게로 최대 value
    for j in range(1,k+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w] + v,dp[i-1][j])
# for d in dp[:n]:
#     print(d[:k+1])
print(dp[n-1][k])