import sys
input = sys.stdin.readline

T = int(input())

def solve():
    n = int(input())
    
    board = []
    for _ in range(2):
        board.append(list(map(int,input().split())))
    
    dp = [[0]*n for _ in range(2)]

    dp[0][0] = board[0][0]
    dp[1][0] = board[1][0]
    
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        return
    
    dp[0][1] = dp[1][0] + board[0][1]
    dp[1][1] = dp[0][0] + board[1][1]

    # dp[i][j] = i,j를 선택했을 때의 최댓값
    for j in range(2,n):
        dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + board[0][j]
        dp[1][j] = max(dp[0][j-1], dp[1][j-2]) + board[1][j]

    print(max(dp[0][n-1], dp[1][n-1]))

for _ in range(T):
    solve()