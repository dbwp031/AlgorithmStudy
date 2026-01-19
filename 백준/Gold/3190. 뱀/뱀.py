N = int(input())
K = int(input())

EMPTY = 0
APPLE = 1

board = [[EMPTY for _ in range(N)] for _ in range(N)]

for _ in range(K):
    i,j = map(int, input().split())
    board[i-1][j-1] = APPLE

L = int(input())
orders = []
for _ in range(L):
    sec, dir = input().split()
    sec = int(sec)
    orders.append([sec, dir])
# 오, 위, 왼, 아
dx = [0,1,0,-1]
dy = [1,0,-1,0]
d = 0

q = []
q.append([0,0])

oi = 0
answer = 0
while q:
    answer +=1
    hx, hy = q[0]
    nx = hx + dx[d]
    ny = hy + dy[d]

    if not (0 <= nx < N and 0 <= ny <N):
        break
    
    crash = False
    for i in range(0, len(q)):
        bx, by = q[i]
        if bx == nx and by == ny:
            crash = True
            break
    if crash:
        break

    q.insert(0, [nx, ny])
    if board[nx][ny] == EMPTY:
        q.pop(len(q)-1)
    elif board[nx][ny] == APPLE:
        board[nx][ny] = EMPTY

    if oi < len(orders) and answer == orders[oi][0]:
        mo = orders[oi][1]
        if mo == "D":
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
        oi += 1

print(answer)