import sys
input = sys.stdin.readline

data = list(map(int,input().split()))
n = data[0]
visited = [[False]*29 for _ in range(29)]
x,y = 14,14

prob = [i/100 for i in data[1:]]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = 0
def isNaive(x,y,naiveProb,time):
    global answer
    
    for i in range(4):
        if prob[i] == 0: continue
        nx,ny = x+dx[i],y+dy[i]
        if not visited[nx][ny]:
            if time+1 == n:
                # print(naiveProb*prob[i])
                answer+= naiveProb*prob[i]
            else:
                visited[nx][ny] = True
                isNaive(nx,ny,naiveProb*prob[i],time+1)
                visited[nx][ny] = False
            
visited[x][y]=True
isNaive(x,y,1,0)
print(answer)
