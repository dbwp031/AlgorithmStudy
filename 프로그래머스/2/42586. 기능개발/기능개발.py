from collections import deque
def solution(progresses, speeds):
    answer = []
    q = deque()
    for i in range(len(progresses)):
        q.append([progresses[i], speeds[i]])
    
    while q:
        while q[0][0] < 100:
            for i in range(len(q)):
                q[i][0] += q[i][1]

        cnt = 0
        while q and q[0][0] >= 100:
            q.popleft()
            cnt += 1
        answer.append(cnt)
    return answer