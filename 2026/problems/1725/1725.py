from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
recs = []
for _ in range(n):
    recs.append(int(input()))

dq = deque()
