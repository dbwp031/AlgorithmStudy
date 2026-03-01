from collections import deque
import heapq
def solution(priorities, location):
    q = deque([(p,i)  for i,p in enumerate(priorities)])
    
    cnt = 0
    while q:
        cp, ci = q.popleft()
        if any([cp < p for p,i in q]):
            q.append((cp,ci))
        else:
            cnt += 1
            if ci == location:
                return cnt