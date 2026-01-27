import sys
sys.setrecursionlimit(100000)

b = []
N = 10
for _ in range(N):
    b.append(list(map(int, input().split())))
INF = 10**9
ans = INF

def checkNxN(b,i,j,n):
    if not (0<=i<=N and 0<=j<=N):
        return False
    if not (0<=i+n<=N and 0<=j+n<=N):
        return False
    
    canPaste = True
    for ii in range(i, i+n):
        for ji in range(j, j+n):
            if b[ii][ji] == 0:
                canPaste = False
                break
    return canPaste

def pasteNxN(b,x,y,n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            b[i][j] = 0
    return b

def detachNxN(b,x,y,n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            b[i][j] = 1
    return b

def checkSuccess(b):
    total = sum([sum(l) for l in b])
    if total == 0:
        return True
    return False

def dfs(tb,x,y,size_count):
    global ans
    # 현재 x,y 처리
    while True:
        if x == 10:
            break
        if tb[x][y] == 1:
            break

        y = (y+1) % 10
        x = x+1 if y == 0 else x
        
    # 만약 x==11이면 최종 계산
    if x == 10:
        if checkSuccess(tb):
            ans = min(ans,sum(size_count))
        return
    
    # b[x][y] == 1인 경우
    # 현재 x,y가 0이면 다음 x,y 값으로 수정
    for i in range(5,0,-1):
        if size_count[i] < 5 and checkNxN(tb,x,y,i):
            tb = pasteNxN(tb,x,y,i)
            size_count[i] += 1
            dfs(tb,x,y,size_count)
            size_count[i] -= 1
            tb = detachNxN(tb,x,y,i)

dfs(b,0,0,[0,0,0,0,0,0])
print(-1 if ans == INF else ans)