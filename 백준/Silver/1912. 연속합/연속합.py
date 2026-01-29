n = int(input())
nums = list(map(int,input().split()))

dp = [0] * len(nums)
if n == 1:
    print(nums[0])
    exit()
    
dp[0] = nums[0]
for i in range(1, len(nums)):
    dp[i] = max(dp[i-1] + nums[i], nums[i])

print(max(dp))