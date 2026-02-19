import sys
input = sys.stdin.readline

n, m = map(int, input().split())
guitars = [0] * n
for i in range(n):
    name, musics = input().split()
    for j in range(m):
        if musics[j] == "Y":
            guitars[i] |= (1 << j)

best_cover = 0
ans = 10**9

for mask in range(1, 1 << n):
    cover = 0
    cnt = bin(mask).count('1')  # 선택한 기타 수
    for bit in range(n):
        if mask & (1 << bit):
            cover |= guitars[bit]
    
    cover_cnt = bin(cover).count('1')  # 커버한 곡 수

    if cover_cnt > best_cover:
        best_cover = cover_cnt
        ans = cnt
    elif cover_cnt == best_cover:
        ans = min(ans, cnt)

print(-1 if best_cover == 0 else ans)