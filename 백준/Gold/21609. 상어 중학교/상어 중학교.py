# BOJ 21609 - 상어 중학교 (정석 구현)
# - 기준 블록: 무지개 제외, (행 최소, 열 최소)
# - 그룹 우선순위: (크기 큰) > (무지개 많은) > (기준행 큰) > (기준열 큰)
# - 무지개(0)는 그룹마다 재사용 가능 → BFS마다만 방문처리

import sys
from collections import deque

input = sys.stdin.readline

EMPTY = -2
BLACK = -1
RAINBOW = 0

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def gravity(a, n):
    for c in range(n):
        write = n - 1
        for r in range(n - 1, -1, -1):
            if a[r][c] == BLACK:
                write = r - 1
            elif a[r][c] != EMPTY:
                v = a[r][c]
                if write != r:
                    a[r][c] = EMPTY
                    a[write][c] = v
                write -= 1


def rotate_ccw(a, n):
    # new[r][c] = old[c][n-1-r]
    return [[a[c][n - 1 - r] for c in range(n)] for r in range(n)]


def bfs_group(a, n, sx, sy, color, visited):
    q = deque([(sx, sy)])
    temp = [[False] * n for _ in range(n)]
    temp[sx][sy] = True
    visited[sx][sy] = True  # 일반 블록만 전역 visited

    cells = [(sx, sy)]
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

    # ✅ 기준 블록: (행 최소, 열 최소)
    std_r, std_c = min(normal_cells)

    # 비교용 튜플: (size, rainbow, std_r, std_c) 를 "큰 것" 선호
    # std는 min으로 잡고, 비교는 큰 std_r/std_c를 선호하므로 그대로 두면 됨.
    return (len(cells), rainbow_cnt, std_r, std_c, cells)


def solve():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    score = 0

    while True:
        visited = [[False] * n for _ in range(n)]
        best = None  # (size, rainbow, std_r, std_c, cells)

        for i in range(n):
            for j in range(n):
                v = board[i][j]
                if v <= 0:  # BLACK, EMPTY, RAINBOW는 시작 불가
                    continue
                if visited[i][j]:
                    continue

                g = bfs_group(board, n, i, j, v, visited)
                if g is None:
                    continue

                # 우선순위대로 "큰" 튜플 선택:
                # size ↑, rainbow ↑, std_r ↑, std_c ↑
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