N,K = map(int,input().split())
data = []
for _ in range(N):
    data.append(list(map(int,input().split())))

dp = [[0] * (K+1) for _ in range(N)]

for i in range(data[0][0], K+1):
    dp[0][i] = data[0][1]

for i in range(1, N):
    w = data[i][0]
    v = data[i][1]
    for j in range(1,K+1):
        if j-w >= 0:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
            
print(max([max(l) for l in dp]))

# for d in dp:
#     print(d)