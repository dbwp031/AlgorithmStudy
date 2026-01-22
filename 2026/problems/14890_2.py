import sys
input = sys.stdin.readline

DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

def check(line, L):
    n = len(line)
    debug(f"HIHI {n}")
    used = [False] * n  # 이 라인에서 경사로가 이미 사용된 칸 표시

    for i in range(n - 1):
        if line[i] == line[i + 1]:
            continue

        diff = line[i + 1] - line[i]

        if abs(diff) != 1:
            return False

        if diff == 1:  # 올라감
            for j in range(i, i - L, -1):
                if j < 0 or line[j] != line[i] or used[j]:
                    return False
                used[j] = True
        else:  # diff == -1 내려감
            for j in range(i + 1, i + 1 + L):
                if j >= n or line[j] != line[i + 1] or used[j]:
                    return False
                used[j] = True

    return True


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0

for r in range(N):
    if check(board[r], L):
        answer += 1

for c in range(N):
    col = [board[r][c] for r in range(N)]
    if check(col, L):
        answer += 1

print(answer)