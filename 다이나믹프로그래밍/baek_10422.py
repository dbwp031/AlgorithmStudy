t = int(input())

for _ in range(t):
    n = int(input())
    dp = [1 for _ in range(n+1)]
    dp[0]=0
    for i in range(n+1):
        if i %2 ==1:
            dp[i]=0
    for i in range(1,n+1):
        if i % 2 ==0:
            if dp[i-2]-1 >=0:
                dp[i]+=dp[i-2] + (dp[i-2]-1)*2
            else:
                dp[i]+=dp[i-2]
    # print(*dp)
    print(dp[-1])