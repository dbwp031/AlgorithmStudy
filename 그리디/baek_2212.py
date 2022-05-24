# 양 옆의 길이를 비교해서 큰거부터 k-1개 빼면 됨.

import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
if k>=n:
    print(0)
else:
    board = list(map(int,input().split()))
    board.sort()
    dist = []
    for i in range(0,n-1):
        dist.append(board[i+1]-board[i])
    dist.sort(reverse=True)
    for i in range(k-1):
        dist.pop(0)
    print(sum(dist))