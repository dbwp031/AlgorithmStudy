n,m,k=map(int,input().split())
# visited = [[False]*n for _ in range(n)]
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

board = [[[]*n]for _ in range(n)]
for _ in range(m):
    r,c,_m,s,d = map(int,input().split())
    r-=1
    c-=1
    board[[r,c]] = [[_m,s,d]]
        
# split
def split(fires):
    mess = 0
    speed = 0
    allOdd = True
    allEven = True
    
    for fire in fires:
        _m,s,d = mess
        mess+=_m
        speed+=s
        if d%2 == 1: allEven = False
        else: allOdd = False
    mess //=5
    speed //=len(fires)
    direction = []
    if allEven or allOdd:
        direction = [0,2,4,6]
    else:
        direction=[1,3,5,7]
    new_fires = []
    for i in range(4):
        new_fires.append([mess,speed,direction[i]])
    return new_fires

for _ in range(k):
    for x in range(n):
        for y in range(n):
            