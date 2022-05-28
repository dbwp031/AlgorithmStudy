n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
board.sort()
dp = [0]*(n)

left = 0
lp = board[0][1]
right = 0
rp = 0
# right cost 해줘야됨.
now = board[0][0]
for i in range(1,n):
    dist = abs(board[i][0]-now)
    right += dist*board[i][1]
    rp +=board[i][1]
popu = left+right
answer = board[0][0]

for i in range(1,n):
    pre = now
    now = board[i][0]
    dist = abs(now-pre)

    left +=dist*lp
    right -=dist*rp
    if popu > left+right:
        popu=left+right
        answer = now
    lp += board[i][1]
    rp -= board[i][1]
print(answer)