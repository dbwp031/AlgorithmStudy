import sys
input = sys.stdin.readline

n,s = map(int,input().split())
nums = list(map(int,input().split()))

cur = 0
l = 0
ans = 10**9
for r in range(n):
    cur += nums[r]
    while cur >= s:
        ans = min(ans, r-l+1)
        cur -= nums[l]
        l += 1
        
if ans == 10**9:
    print(0)
else:
    print(ans)
