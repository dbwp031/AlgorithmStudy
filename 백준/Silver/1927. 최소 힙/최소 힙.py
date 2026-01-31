import sys
import heapq
input = sys.stdin.readline

N = int(input())
hq = []
answer = []

for _ in range(N):
    op = int(input())
    if op == 0:
        if hq:
            answer.append(heapq.heappop(hq))
        else:
            answer.append(0)
    else:
        heapq.heappush(hq, op)
for a in answer:
    print(a)