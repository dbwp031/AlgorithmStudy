from collections import deque
n,k=map(int,input().split())
q = deque([[n,0]])
count = [0]*100001
visited = [False]*100001
visited[n]=0
finds=False
while q and not finds:
    for _ in range(len(q)):
        
        now,time = q.popleft()
        if now == k:
            finds = True
        if now-1>=0:
            if visited[now-1] == False:
                visited[now-1] = time+1
                count[now-1]+=1
                q.append([now-1,time+1])
            elif visited[now-1] == time+1:
                count[now-1]+=1
        if now+1<=100000:
            if visited[now+1] == False:
                visited[now+1] = time+1
                count[now+1]+=1
                q.append([now+1,time+1])
            elif visited[now+1] == time+1:
                count[now+1]+=1
        if now*2<=100000:
            if visited[now*2] == False:
                visited[now*2] = time+1
                count[now*2]+=1
                q.append([now*2,time+1])
            elif visited[now*2] == time+1:
                count[now*2]+=1
print(visited[k])
print(count[k])