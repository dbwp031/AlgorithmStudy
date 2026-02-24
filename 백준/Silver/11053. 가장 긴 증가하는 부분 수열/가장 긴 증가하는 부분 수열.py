import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [1] * 1_000
# dp[i] = i번째까지 고려했을 때, 최고 LIS 길이
for i in range(1, n):
    cur = nums[i]
    for j in range(0, i):
        if nums[j] < cur:
            dp[i] = max(dp[i], dp[j]+1)
# print(dp[:n])
print(max(dp[:n]))