import sys
input = sys.stdin.readline


def solve(k,n):
    board = [[0] * (n+1) for _ in range(k+1)]
    
    # 1. 1층 세팅
    for i in range(n+1):
        board[0][i] = i
    
    # 2. 각 층 세팅
    for i in range(1, k+1):
        for j in range(1, n+1):
            ssum = 0
            for line in range(1, j+1):
                ssum += board[i-1][line]
            board[i][j] = ssum
    return board[k][n]    
    
if __name__ == "__main__":
    T = int(input())
    K_N = []
    for _ in range(T):
        k = int(input())
        n = int(input())
        K_N.append((k,n))
    
    for (k,n) in K_N:
        print(solve(k,n))   
    