¡import sys
from collections import deque

input = sys.stdin.readline

EMPTY = -2
WALL = -1
RAINBOW = 0

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


class Group:
    """
    BOJ 21609 (상어 중학교) 블록 그룹
    우선순위(최대 선택):
      1) 그룹 크기 큰 것
      2) 무지개 블록 수 큰 것
      3) 기준 블록 행 큰 것
      4) 기준 블록 열 큰 것
    기준 블록: 무지개(0)가 아닌 블록 중 '행이 가장 큰', 그 중 '열이 가장 큰' 블록
    """

    __slots__ = ("cells", "size", "rainbows", "std_r", "std_c")

    def __init__(self, cells, size, rainbows, std_r, std_c):
        self.cells = cells
        self.size = size
        self.rainbows = rainbows
        self.std_r = std_r
        self.std_c = std_c

    def __lt__(self, other):
        if self.size != other.size:
            return self.size < other.size
        if self.rainbows != other.rainbows:
            return self.rainbows < other.rainbows
        if self.std_r != other.std_r:
            return self.std_r < other.std_r
        return self.std_c < other.std_c


def gravity(board, n):
    """
    중력 적용:
      - EMPTY(-2)는 빈칸
      - WALL(-1)은 벽(고정, 벽 아래로는 못 내려감)
      - 그 외 블록은 가능한 아래로 떨어짐
    """
    for c in range(n):
        write = n - 1
        for r in range(n - 1, -1, -1):
            if board[r][c] == WALL:
                write = r - 1
            elif board[r][c] != EMPTY:
                val = board[r][c]
                if write != r:
                    board[r][c] = EMPTY
                    board[write][c] = val
                write -= 1
    return board


def rotate_90_left(board, n):
    """
    반시계 90도 회전:
    new[r][c] = old[c][n-1-r]
    """
    return [[board[c][n - 1 - r] for c in range(n)] for r in range(n)]


def find_best_group(board, n):
    """
    전체 보드에서 '가장 큰 블록 그룹'을 찾아 Group 반환.
    그룹 조건:
      - 일반 블록(1~M) + 무지개(0)
      - 일반 블록 색은 시작점 색과 동일
      - 무지개는 어떤 색과도 묶일 수 있음
      - 그룹 크기 >= 2
    방문 처리(정석):
      - 일반 블록은 전역 visited로 재시작 방지
      - 무지개 블록은 BFS마다 방문했더라도 전역 visited에 묶지 않음
    """
    visited = [[False] * n for _ in range(n)]
    best = None

    for i in range(n):
        for j in range(n):
            color = board[i][j]
            if color <= 0:  # WALL(-1), EMPTY(-2), RAINBOW(0) 시작 불가
                continue
            if visited[i][j]:
                continue

            q = deque([(i, j)])
            temp = [[False] * n for _ in range(n)]
            temp[i][j] = True
            visited[i][j] = True  # 일반 블록은 전역 방문

            cells = [(i, j)]
            rainbow_cells = []
            # 기준 블록 후보(무지개 제외)만 모아서 기준 블록 계산
            normal_cells = [(i, j)]

            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if not (0 <= nx < n and 0 <= ny < n):
                        continue
                    if temp[nx][ny]:
                        continue

                    v = board[nx][ny]
                    if v == color or v == RAINBOW:
                        temp[nx][ny] = True
                        q.append((nx, ny))
                        cells.append((nx, ny))

                        if v == RAINBOW:
                            rainbow_cells.append((nx, ny))
                        else:
                            normal_cells.append((nx, ny))
                            if not visited[nx][ny]:
                                visited[nx][ny] = True

            size = len(cells)
            if size < 2:
                continue

            # 기준 블록: normal_cells 중 (행 최대, 열 최대)
            std_r, std_c = max(normal_cells)  # 튜플 비교: (r, c) 기준

            g = Group(
                cells=cells,
                size=size,
                rainbows=len(rainbow_cells),
                std_r=std_r,
                std_c=std_c,
            )

            if best is None or best < g:
                best = g

    return best


def remove_group(board, group):
    for r, c in group.cells:
        board[r][c] = EMPTY


def solve():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    score = 0
    while True:
        best = find_best_group(board, N)
        if best is None:
            break

        score += best.size * best.size
        remove_group(board, best)

        gravity(board, N)
        board = rotate_90_left(board, N)
        gravity(board, N)

    print(score)


if __name__ == "__main__":
    solve()