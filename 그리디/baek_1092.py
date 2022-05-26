# 약간 n포인터 느낌아닌가? => 약간은 다름
# 커버할 수 있는 크레인의 수가 증가할 때마다 계산 한번씩 때리면 될듯 나누기 막 해서

n = int(input())
crain_power = list(map(int,input().split()))
m = int(input())
boxes = list(map(int,input().split()))

boxes.sort(reverse=True)
crain_power.sort(reverse=True)

pointer = []
visited = [False]*m
for i in range(n):
    nothing = True
    for j in range(m):
        if crain_power[i]>=boxes[j]:
            pointer.append(j)
            nothing=False
            break
    if nothing==True:
        pointer.append(m)

day = 0
count = m
if pointer[0]!=0:
    print(-1)
else:
    while count >0:
        day+=1
        # print(pointer)
        # print(visited)
        for i in range(n):
            while True:
                if pointer[i]==m: break
                elif visited[pointer[i]]:
                    pointer[i]+=1
                else:
                    visited[pointer[i]]=True
                    count-=1
                    break
    print(day)