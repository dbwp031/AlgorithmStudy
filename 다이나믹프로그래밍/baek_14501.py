# 일단 다이나믹 프로그래밍은 점화식을 기반으로 생각을 해야합니다.
# 그런데 제가 예전에 풀어본 기억을 토대로하면, 그냥 dp table을 미리 작성하고, 그거에 맞춰서 점화식을 찾아내는게 더 빠르긴 했습니다.

n = int(input())
dp=[0]*(n+2)
for now_day in range(1,n+1):
    now_cost,now_money = map(int,input().split())
    if now_day + now_cost<=n+1 and dp[now_day + now_cost] < dp[now_day]+now_money:
        for d in range(now_day + now_cost,n+2):
            dp[d] = max(dp[d],dp[now_day]+now_money)
print(dp[n+1])