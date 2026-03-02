import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while scoville[0] < K and len(scoville) > 1:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        cnt+=1
    if scoville[0] >= K:
        return cnt
    else:
        return -1
        
