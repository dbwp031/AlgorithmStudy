import sys
from collections import deque
input = sys.stdin.readline

tcs = []
for _ in range(int(input())):
    tcs.append(list(map(int,input().split())))

for tc in tcs:
    f, t = tc
    visited = [False] * 10000
    q = deque()
    
    q.append((f,""))
    visited[f] = True
    
    while q:
        cf, ct = q.popleft()
        if cf == t:
            print(ct)
            break
        
        nf = cf*2 % 10000 # D
        if not visited[nf]:
            visited[nf] = True
            q.append((nf, ct+"D"))
        
        nf = cf-1 if cf-1>=0 else 9999
        if not visited[nf]:
            visited[nf] = True
            q.append((nf, ct+"S"))
        
        nf = (cf % 1000)*10 + (cf // 1000) # 0001 -> 0010 / 1234 -> 2341
        if not visited[nf]:
            visited[nf] = True
            q.append((nf, ct+"L"))
        
        nf = (cf // 10) + (cf % 10)*1000 # 1234 -> 4123
        if not visited[nf]:
            visited[nf]=True
            q.append((nf, ct+"R"))
    
