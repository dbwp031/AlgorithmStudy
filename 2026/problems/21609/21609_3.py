
import sys
from collections import deque

input = sys.stdin.readline

EMPTY = -2
BLACK = -1
RAINBOW = 0
# 오 위 왼 아
dx = (0,1,0,-1)
dy = (1,0,-1,0)

def gravity(a, n):
    for c in range(n):
        write = n-1
        for r in range(n-1, -1, -1):
            if a[r][c] == BLACK:
                write = r-1
            elif a[r][c] != EMPTY:
                v = a[r][c]
                if write != r:
                    a[r][c] = EMPTY
                    a[write][c] = v
                write -= 1

def rotate_ccw(a, n):
    return [[a[c][n-1-r] for c in range(n)] for r in range(n)]

def bfs_group(a, n, sx, sy, color, visited):
    q = deque([(sx, sy)])
    temp = [[False] * n for _ in range(n)]
    temp[sx][sy] = True
    visited[sx][sy] = True

    cells = [(sx,sy)]
    normal_cells = [(sx, sy)]
    rainbow_cnt = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if temp[nx][ny]:
                continue
            
            v = a[nx][ny]
            if v == color or v == RAINBOW:
                temp[nx][ny] = True
                q.append((nx, ny))
                cells.append((nx, ny))

                if v == RAINBOW:
                    rainbow_cnt += 1
                else:
                    normal_cells.append((nx, ny))
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
    if len(cells) < 2:
        return None
    
    std_r, std_c = min(normal_cells)
    return (len(cells), rainbow_cnt, std_r, std_c , cells)

def solve():
    n,m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    score = 0

    while True:
        visited = [[False] * n for _ in range(n)]
        best = None

        for i in range(n):
            for j in range(n):
                v = board[i][j]
                if v<=0:
                    continue
                if visited[i][j]:
                    continue
                
                g = bfs_group(board, n, i, j, v, visited)
                if g is None:
                    continue
                
                # g[0], g[1], g[2], g[3] 우선순위대로 "큰" 튜플 선택:
                if best is None or g[:4] > best[:4]:
                    best = g
        if best is None:
            break

        size, _, _, _, cells = best
        score += size * size

        for x, y in cells:
            board[x][y] = EMPTY
        
        gravity(board, n)
        board = rotate_ccw(board, n)
        gravity(board, n)
    print(score)

if __name__ == "__main__":
    solve()