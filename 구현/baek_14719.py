import sys
input = sys.stdin.readline
h,w = map(int,input().split())
data = list(map(int,input().split()))

AIR = 0
BLOCK = 1
visited = [[False for _ in range(w)] for _ in range(h)]

board = [[AIR for _ in range(w)] for _ in range(h)]
for i in range(w):
    for j in range(h-data[i], h):
        board[j][i] = BLOCK
# for b in board:
#     print(b)

def 해당_위치가_비가_찰_수_있는_칸인가(x,y):
    assert board[x][y] == AIR
    ny = y
    canWaterLeft = False
    canWaterRight = False
    canWater = False
    while(ny>=0):
        if board[x][ny] == BLOCK:
            canWaterLeft = True
            break
        ny -=1
    ny = y
    while(ny<w):
        if board[x][ny] == BLOCK:
            canWaterRight = True
            break
        ny +=1
        
    if canWaterLeft and canWaterRight:
        canWater = True
    
    return canWater

answer = 0
for i in range(h):
    for j in range(w):
        if board[i][j]==AIR and 해당_위치가_비가_찰_수_있는_칸인가(i,j):
            answer+=1
print(answer)
