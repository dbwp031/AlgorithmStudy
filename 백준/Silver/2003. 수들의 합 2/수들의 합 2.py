import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = list(map(int,input().split()))

cnt = 0
cur = 0
l = 0
for r in range(n):
    cur += nums[r]
    while cur > m and l <= r:
        cur -= nums[l]
        l += 1
    if cur == m:
        cnt += 1
print(cnt)