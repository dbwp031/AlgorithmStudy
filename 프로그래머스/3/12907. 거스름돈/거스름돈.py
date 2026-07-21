def solution(n, money):
    # dp[i] = i원을 지불하는 총 가짓 수
    dp = [0] * (n+1)
    
    for m in money:
        dp[m] += 1
        for w in range(m+1, n+1):
            dp[w] += dp[w-m]
    #     print(m, dp)
    # print(dp)
    return dp[-1]
    # def solution(n, money):
#     # dp[i] = i원을 지불하는 총 가짓 수
#     dp = [0] * (n+1)
    
#     for m in money:
#         dp[m] = 1
#     print(dp)
#     for i in range(len(dp)):
#         for m in money:
#             prev = i - m
#             if prev <= 0:
#                 continue
#             else:
#                 dp[i] += dp[prev]
#     print(dp)
#     return dp[n]