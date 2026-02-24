import sys
input = sys.stdin.readline

def solve(n,m):
    dp = [[0]*m for _ in range(n)]
    # dp[i][j] = i번째 노드까지 고려했을 때, 
    # N_i -> M_j를 선택했을 때 가능한 경우의 수
    dp[0][0] = 1
    for i in range(1, m-n+1):
        dp[0][i] = dp[0][i-1] + 1
    
    for i in range(1, n):
        for j in range(i,m-n+1+i):
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    # for d in dp:
    #     print(d)
    print(dp[n-1][m-1])

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    solve(n,m)
