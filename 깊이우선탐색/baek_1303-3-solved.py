n,m = map(int,input().split())
board = []
for _ in range(m):
    board.append(list(input()))
wp = 0
bp = 0

visited = [[False]*n for _ in range(m)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y,team,count):
    visited[x][y]=True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<m and 0<=ny<n and visited[nx][ny]==False and board[nx][ny]==team:
            # 레전드 여기가 키 포인트다. count를 return 해주는데, 이 업데이트 된 count가 다른 dfs에 들어가게 된다.
            # 내가 평소에 하던 방법은 최대 count를 전역 변수에 따로 저장해주었다.
            # 이 코드는 count라는 값을 return해준다.
            # (1) 만약 count를 return해서 이 count를 계속 업데이트를 해주면 탐색한 수가 계속 커짐. => 전체 개수 구하는거에 사용하면 됨.
            # (2) 만약에 count를 업데이트 하지 않으면, 다른 곳을 탐색하고 돌아와도 현재까지의 개수가 유지됨.
            # 간단하게 설명하면 현재 3번째 칸임. 즉 카운트가 3
            # 만약 (1)번 방법을 쓰면, 한번 dfs로 쭉 2칸 더 들어갔다 나오면 카운트가 5로 업데이트 됨. 그래서 최대 개수를 알 수 있음.
            # 반대로 (2)번 쓰면, dfs로 들어갔다 나와도 카운트가 현재의 상태인 3이 유지됨.
            # 이 특징은 dfs 뿐 아니라 일반 재귀함수에 대한 특징이니까 잘 기억해두는게 좋을듯!!
            count = dfs(nx,ny,team,count+1) 
    return count

for i in range(m):
    for j in range(n):
        if visited[i][j] == False:
            if board[i][j]=='W':
                wp += dfs(i,j,'W',1)**2
            else:
                bp += dfs(i,j,'B',1)**2
print(wp,bp)
            