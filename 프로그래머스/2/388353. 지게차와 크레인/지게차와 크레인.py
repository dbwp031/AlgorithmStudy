from collections import deque

def solution(storage, requests):
    N = len(storage)
    M = len(storage[0])
    answer = N*M
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    # 비어있는 값은 -
    def is_open(storage, x, y):
        N = len(storage)
        M = len(storage[0])
        q = deque()
        q.append((x,y))
        visited = [[False] * (M) for _ in range(N)]
        while q:
            a,b = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                # 바깥 연결 확인
                if not (0<=nx<N and 0<=ny<M):
                    return True
                elif not visited[nx][ny] and storage[nx][ny] == "-":
                    q.append((nx,ny))
                    visited[nx][ny] = True
        return False
        
    storage = [list(s) for s in storage]
    for request in requests:
        target = request[0]
        op = len(request) # 1-> 지게차 2-> 크레인
        if op == 2:
            for i in range(N):
                for j in range(M):
                    if storage[i][j] == target:
                        storage[i][j] = "-"
                        answer -= 1
        elif op == 1:
            temp = []
            for i in range(N):
                for j in range(M):
                    if storage[i][j] == target and is_open(storage,i,j):
                        temp.append((i,j))
                        answer -= 1
            for tx, ty in temp:
                storage[tx][ty] = "-"
    for s in storage:
        print(s)
    return answer