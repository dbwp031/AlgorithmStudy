import sys
import heapq
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

heapq.heapify(nums)

answer = 0
while nums:
    if len(nums) >= 2:
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        answer += (a+b)
        heapq.heappush(nums, (a+b))
    else:
        a = heapq.heappop(nums)
print(answer)
