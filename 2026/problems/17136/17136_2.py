import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = 10
b = [list(map(int, input().split())) for _ in range(N)]
INF = 10**9
ans = INF

def can_paste(x, y, n):
    if x + n > 10 or y + n > 10:
        return False
    for i in range(x, x+n):
        for j in range(y, y+n):
            if b[i][j] == 0:
                return False
    return True

def paste(x, y, n, v):
    for i in range(x, x+n):
        for j in range(y, y+n):
            b[i][j] = v

def dfs(idx, used, left, cnt):
    global ans
    if used >= ans:
        return
    if left == 0:
        ans = min(ans, used)
        return
    if idx == 100:
        return

    x, y = divmod(idx, 10)

    if b[x][y] == 0:
        dfs(idx+1, used, left, cnt)
        return

    # b[x][y] == 1
    for n in range(5, 0, -1):
        if cnt[n] == 5:
            continue
        if can_paste(x, y, n):
            paste(x, y, n, 0)
            cnt[n] += 1
            dfs(idx+1, used+1, left - n*n, cnt)
            cnt[n] -= 1
            paste(x, y, n, 1)

left = sum(sum(row) for row in b)
cnt = [0]*6
dfs(0, 0, left, cnt)
print(-1 if ans == INF else ans)