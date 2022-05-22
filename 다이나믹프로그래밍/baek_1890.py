# 간단한 이차원 dp 문제입니다.
# 이문제에서 얻어갈 만한 아이디어는 "접근을 오른쪽, 아래로만 한다면, 순차적으로 접근하면 해당 인덱스는 최적을 보장한다"입니다.
# 이 문제에서 아래, 오른쪽으로만 뛸 수 있다고 했습니다. 그렇기 때문에 순차적으로 접근하고 dp를 사용하면 최대 값을 보장 할 수 있었습니다.

n = int(input())
board = []
dp = [[0]*n for _ in range(n)]
dp[0][0]=1
for _ in range(n):
    board.append(list(map(int,input().split())))
# 오 아
dx = [0,1]
dy = [1,0]
for x in range(n):
    for y in range(n):
        if dp[x][y]!=0 and not (x==n-1 and y==n-1):
            for d in range(2):
                nx = x + dx[d]*board[x][y]
                ny = y + dy[d]*board[x][y]
                if 0<=nx<=n-1 and 0<=ny<=n-1:
                    dp[nx][ny]+=dp[x][y]
        # for d in dp:
        #     print(*d)
        # print('----')
print(dp[n-1][n-1])