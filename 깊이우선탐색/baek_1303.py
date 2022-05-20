n,m = map(int,input().split())
board = []
for _ in range(m):
    board.append(list(input()))
wp = 0
bp = 0
# 첫번째 드는 생각
# 이 count를 dfs의 변수로 넣어줘야 하나?
# 그렇다면 return 탈출 조건을 만족하면 global count값과 현재 count값을 max로 비교해줌으로써 사용할 수 있다.
# 만약 변수로 사용하지 않는다면, => 구현할 수 없을 것 같다.
# 왜냐하면 그렇다면 dfs함수가 들어갈때마다 +1이 되는 방식으로 구현해야 할텐데, 이렇게 되면 올바른 답을 찾을 수 없다.

# 많은 변수들이 파라미터로 들어가는게 좋은 듯? 물론 과하면 안 좋은듯 

# 이런 그냥 탐색만 하면 되는 문제
# bfs: 탐색을 하되, 특정 지점에 최소로 도착하는 시간을 알 수 있음.
# dfs: 탐색을 하되, 가장 깊숙히 들어갈 수 있음.
# 만약 브루트포스 탐색이면 그냥 구현 쉬워보이는게 좋은 듯.
# 만약 특정 지점까지의 최소 거리: bfs
# 백트래킹: dfs 
# => 백트래킹이 필요한 dfs나 탈출 조건이 까다로운 dfs 구현 아직 어려워함.

#bfs는 그냥 visited를 한번하면 다시 되돌리지 않아도 됨. 왜냐하면 그곳을 다시 방문하지 않으니깐
# 하지만 dfs는 다시 방문해야함. 그래서 visited를 True / False 계속 바꿔줘야하는데 어떻게 처리해야 하지?


wcnt=bcnt=0

visited = [[False]*n for _ in range(m)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y,team,count):
    global wcnt,bcnt
    if not (0<=x<=m-1 and 0<=y<=n-1) or board[x][y]!=team or visited[x][y]: # 우선 탈출 조건에서 이미 방문했다면 탈출
        if team == "W": wcnt = max(wcnt,count)
        elif team =="B": bcnt = max(bcnt,count)
        return
    # 탈출 조건에 부합하지 않으면 방문 처리해줌.
    visited[x][y]=True
    # 깊이 +1
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        dfs(nx,ny,team,count+1)
    # 깊이 다 돌면 방문안함처리. => 이렇게 했더니 나중에 다 끝나고 나왔을 때 방문처리가 하나도 되어있지 않음.
    visited[x][y]=False
wp=bp=0
for i in range(m):
    for j in range(n):
        if visited[i][j]==False:
            wcnt=bcnt=0
            dfs(i,j,board[i][j],1)
            if board[i][j]=="W":
                wp += wcnt**2
            else:
                bp += bcnt**2    
print(wp,bp)

# 지금까지 내가 생각한 dfs의 이미지는 뱀처럼 1부터 N까지 가고 다시 0으로가서 새로운 1~N(혹은 최대 깊이)를 방문하는 거라고 생각했다.
# 하지만 dfs는 (현재 기준) 최대 깊이 1이 끝나면, 최대 깊이2를 방문한다.
# 무슨뜻이냐 3 ->5 / 3->6/ 3->5 약간 이런 느낌.
# 