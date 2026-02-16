import sys
import heapq
input = sys.stdin.readline

n = int(input())

hq = []
answer = []
for _ in range(n):
    op = int(input())
    if op == 0:
        if len(hq) == 0:
            answer.append(0)
        else:
            answer.append(heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq, (op * -1, op))
# print("---")
for a in answer:
    print(a)