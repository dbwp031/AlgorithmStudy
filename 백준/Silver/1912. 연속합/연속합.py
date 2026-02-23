import sys
input = sys.stdin.readline

n = int(input())
nums = [0] + list(map(int,input().split()))
dp = [0] * (n+1)
for i, num in enumerate(nums):
    if i == 0:
        continue
    dp[i] = max(dp[i-1], 0) + num

# print(dp[1:])
print(max(dp[1:]))