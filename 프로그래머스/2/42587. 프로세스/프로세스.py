from collections import deque
import heapq
def solution(priorities, location):
    
    q = deque()
    pq = []
    for i in range(len(priorities)):
        q.append((priorities[i], location == i))
        heapq.heappush(pq, -priorities[i])
    
    cnt = 0 
    while pq:
        p = -heapq.heappop(pq)
        # print(p)
        while q:
            cp, is_target = q.popleft()
            if p == cp:
                cnt += 1
                if is_target:
                    return cnt
                break
            else:
                q.append((cp, is_target))
                