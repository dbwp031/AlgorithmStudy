N,M = map(int,input().split())
b = []
b.append([0]*(N+1))
for _ in range(N):
    b.append([0] + list(map(int,input().split())))

ops = []
for _ in range(M):
    ops.append(list(map(int,input().split())))

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

clouds = [(N-1,1), (N-1,2), (N,1),(N,2)]
increased = []
def move_clouds(order_index):
    global clouds, ops, b
    di,si = ops[order_index]
    di = di-1
    for i in range(len(clouds)):
        x,y = clouds[i]
        nx,ny = (x + dx[di]*si) % (N) + 1, (y + dy[di]*si )  % (N) + 1
        print(nx,ny)
        clouds[i] = (nx,ny)

def rain():
    global clouds, b, increased
    for x,y in clouds:
        b[x][y] +=1

side_dx = [-1,-1,1,1]
side_dy = [-1,1,-1,1]

def copy_water():
    global b
    for x,y in clouds:
        add = 0
        for k in range(4):
            nx = x + side_dx[k]
            ny = y + side_dy[k]

            if 1<=nx<=N and 1<=ny<=N:
                add += b[nx][ny]
        b[x][y] += add
def remove_and_new_clouds():
    global b, clouds
    new_clouds = []
    for i in range(1,N+1):
        for j in range(1,N+1):
            if b[i][j] >= 2 and (i,j) not in clouds:
                new_clouds.append((i,j))
                b[i][j] -=2
    clouds = new_clouds

for i in range(len(ops)):
    move_clouds(i)
    rain()
    copy_water()
    remove_and_new_clouds()

print(sum([sum(row) for row in b]))