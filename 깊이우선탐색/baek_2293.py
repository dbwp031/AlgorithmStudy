# dfs로 구현하면 될 줄 알았는데, 시간 초과가 났다.
import sys
sys.setrecursionlimit(int(1e6))
n,k = map(int,input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
# # 그냥 전체 개수만 구하면 되니깐, count는 global로
# coin.sort()
# count = 0
# def dfs(pointer,now):
#     global count
#     if now > k: return
#     elif now == k:
#         count+=1
#         return
#     else:
#         for i in range(pointer,n):
#             dfs(i,now+coin[i])
# dfs(0,0)
# print(count)

# dp로 구현하면 아래일 것입니다.
from collections import deque
n,k = map(int,input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
deque.append([0,0])
dp = [0]*10001
for i in range()
