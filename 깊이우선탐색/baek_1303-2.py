# 깊이우선탐색/baek_1303 + baek_1303-2 에서 구현한 dfs 방식은 결국 무조건 한 붓 그리기이다.
# 그래서 탐색으론 올바르지 않은 상황이다. 내가 dfs에 대해서 풀어야 할 오해는 뭐지?
n,m = map(int,input().split())
board = []
for _ in range(m):
    board.append(list(input()))
wp = 0
bp = 0
wcnt=bcnt=0

visited = [[False]*n for _ in range(m)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
real_visited = [[False]*n for _ in range(m)]
def dfs(x,y,team,count):
    visited[x][y]=True
    real_visited[x][y]=True
    global wcnt,bcnt
    if team == "W": wcnt = max(wcnt,count)
    elif team =="B": bcnt = max(bcnt,count)
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        if (0<=nx<=m-1 and 0<=ny<=n-1) and visited[nx][ny]==False and board[nx][ny]==team:
            dfs(nx,ny,team,count+1)
            visited[nx][ny]=False
    # 깊이 다 돌면 방문안함처리. => 이렇게 했더니 나중에 다 끝나고 나왔을 때 방문처리가 하나도 되어있지 않음.
    visited[x][y]=False
wp=bp=0
for i in range(m):
    for j in range(n):
        if real_visited[i][j]==False:
            wcnt=bcnt=0
            dfs(i,j,board[i][j],1)
            print(board[i][j],wcnt,bcnt)
            if board[i][j]=="W":
                wp += wcnt**2
            else:
                bp += bcnt**2    
print(wp,bp)

# 지금까지 내가 생각한 dfs의 이미지는 뱀처럼 1부터 N까지 가고 다시 0으로가서 새로운 1~N(혹은 최대 깊이)를 방문하는 거라고 생각했다.
# 하지만 dfs는 (현재 기준) 최대 깊이 1이 끝나면, 최대 깊이2를 방문한다.
# 무슨뜻이냐 3 ->5 / 3->6/ 3->5 약간 이런 느낌.
# 