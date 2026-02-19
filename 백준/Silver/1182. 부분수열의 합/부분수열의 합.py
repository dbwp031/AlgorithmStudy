from itertools import combinations
import sys
input = sys.stdin.readline

def get_powerset(nums):
    powerset = []
    for i in range(1, len(nums)+1):
        for comb in combinations(nums, i):
            powerset.append(comb)
    return powerset

n,s = map(int,input().split())
nums = list(map(int,input().split()))
cnt = 0
for subset in get_powerset(nums):
    # print(subset)
    if sum(subset) == s:
        cnt += 1
print(cnt)