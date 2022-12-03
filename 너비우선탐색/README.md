### 참고할만한 사이트 
[DFS BFS 필수 문제](https://www.acmicpc.net/workbook/view/1983)


### 기본적인 구현 [문제]()
```           
# bfs
count = 0
queue = [] # 간단하게 queue를 사용할 땐 list로 선언.
while queue:
    x,y= queue.pop(0) # queue.pop(0)로 deque
    count += search(x,y)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and grid[nx][ny]==1 and not visited[nx][ny]:
            queue.append([nx,ny]) # queue.append로 enque
            visited[nx][ny]=True # ** visited 처리가 필요할 시엔, enque시에 visit 처리해줘야 함.
                                 # 만약 deque때 visit처리하면 해당 노드가 여러번 들어감.

return count
```
