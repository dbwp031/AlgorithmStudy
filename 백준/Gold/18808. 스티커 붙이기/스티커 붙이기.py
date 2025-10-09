
def canSet(i, j, sticker):
  r, c = len(sticker), len(sticker[0])

  # 경계 체크: 끝 인덱스는 배제이므로 > 로 비교
  if i + r > n or j + c > m:
      return False

  # 스티커가 1인 칸만 충돌 검사
  for si in range(r):
      for sj in range(c):
          if sticker[si][sj] == 1 and board[i + si][j + sj] == 1:
              return False
  return True

def setSticker(i, j, sticker):
  r, c = len(sticker), len(sticker[0])
  for ci in range(i, i + r):
      for cj in range(j, j + c):
          # 스티커가 1인 칸만 보드에 부착
          if sticker[ci - i][cj - j] == 1:
              board[ci][cj] = 1
            
def check_and_set(sticker):
  for i in range(n):
      for j in range(m):
          if canSet(i, j, sticker):
              setSticker(i, j, sticker)
              return True
  return False

  
def rotate_matrix_90(matrix):
  # 시계 방향 90도 회전
  return [list(reversed(col)) for col in zip(*matrix)]
  
n, m, k = map(int, input().split())
stickers = []
for _ in range(k):
  r, c = map(int, input().split())
  sticker = []
  for _ in range(r):
    sticker.append(list(map(int, input().split())))
  stickers.append(sticker)

board = [[0] * m for _ in range(n)]

for s in range(len(stickers)):
  for _ in range(4):
    if check_and_set(stickers[s]):
      break
    else:
      stickers[s] = rotate_matrix_90(stickers[s])

ssum = 0
for line in board:
    ssum += sum(line)
print(ssum)