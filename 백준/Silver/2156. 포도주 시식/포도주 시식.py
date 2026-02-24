import sys
input = sys.stdin.readline

# 고려했을 때, 선택했을 때 의 차이가 무엇인지?
# 연속된 3개의 포도주를 마실 수 없다. => dp[i]를 계산할 때, i-1, i-2가 마셨는지, 안마셨는 지를 알고 있어야한다.
# 즉, i번째 위치에서 i번째의 선택 여부가 추후 판단에 영향을 미칠때 "선택했을 때"임.
n = int(input())
grapes = []
for _ in range(n):
    grapes.append(int(input()))

# dp[i][0] = i번째 원소까지 고려하고, i번째를 안마셨을 때 가능한 최댓값
# dp[i][1] = i번째 원소까지 고려하고, i번째를 마셨을 때 가능한 최댓값

dp = [[0]*2 for _ in range(10_000)]
dp[0][1] = grapes[0]
for i in range(1,n):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1])
    dp[i][1] = max(dp[i-2][0] + grapes[i-1] + grapes[i], dp[i-1][0] + grapes[i])
# print(grapes)
# print(dp[:n])
print(max(dp[n-1]))
