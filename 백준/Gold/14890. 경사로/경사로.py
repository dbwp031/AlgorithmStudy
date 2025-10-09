import sys
input = sys.stdin.readline

n, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def check(nums):
    visited = [False] * n
    for i in range(n - 1):
        diff = nums[i + 1] - nums[i]
        if diff == 0:
            continue
        if abs(diff) > 1:
            return False

        # 오르막: 뒤로 L칸 필요 (높이 = nums[i])
        if diff == 1:
            for k in range(L):
                pos = i - k
                if pos < 0: return False
                if nums[pos] != nums[i]: return False
                if visited[pos]: return False
                visited[pos] = True

        # 내리막: 앞으로 L칸 필요 (높이 = nums[i+1])
        else:  # diff == -1
            for k in range(1, L + 1):
                pos = i + k
                if pos >= n: return False
                if nums[pos] != nums[i + 1]: return False
                if visited[pos]: return False
                visited[pos] = True
    return True

ans = 0
# 가로
for r in range(n):
    if check(board[r]):
        ans += 1
# 세로
for c in range(n):
    col = [board[r][c] for r in range(n)]
    if check(col):
        ans += 1

print(ans)