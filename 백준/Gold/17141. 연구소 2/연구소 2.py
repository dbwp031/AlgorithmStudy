# 이 문제의 최대 복잡도를 어떻게 봐야하지?
# 최대: n*nC10 * n*n = n^4 = 625 * 10^4
# 파이썬: 1초에 2천만번 = 2 * 10^7

from collections import deque
import itertools
from copy import deepcopy
n, m = map(int, input().split())
board = []
for _ in range(n):
  board.append(list(map(int, input().split())))

# queue에 담아서 bfs하면 된다.
dx = [0,1,0,-1]
dy = [1,0,-1,0]

start_points_all = []
for i in range(n):
  for j in range(n):
    if board[i][j] == 2:
      start_points_all.append((i,j,0))

def step(start_points, board):
  total_cost = -1
  for point in start_points:
    x, y,cost = point
    board[x][y] = -1
  q = deque(start_points)
  while q:
    # print(q)
    x,y,cost = q.popleft()
    # print(f"Cost: {cost}")
    total_cost = max(total_cost, cost)
    for i in range(4):
      nx, ny = x + dx[i], y+dy[i]
      if not (0<=nx<n) or not (0<=ny<n):
        continue
      elif board[nx][ny] in (1,-1):
        continue
      board[nx][ny] = -1
      q.append((nx,ny,cost+1))
  for i in range(n):
    for j in range(n):
      if board[i][j] in (0,2):
        total_cost = -1
        break
  return total_cost

result = 1e7
comb = itertools.combinations(start_points_all, m)
for c in comb:
  b = deepcopy(board)
  step_result = step(list(c),b)
  if step_result != -1:
    result = min(result,step_result)

if result == 1e7:
  print(-1)
else:
  print(result)