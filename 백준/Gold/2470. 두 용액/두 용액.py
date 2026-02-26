import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
nums.sort()

l, r = 0, n-1
mix_v = 10**9*2+1
ans = [-1,-1]
while l < r:
    s = nums[l] + nums[r]
    if abs(s) < abs(mix_v):
        mix_v = s
        ans = [nums[l],nums[r]]
    if s == 0:
        break
    elif s > 0:
        r -= 1
    else:
        l += 1
ans.sort()
print(f"{ans[0]} {ans[1]}")