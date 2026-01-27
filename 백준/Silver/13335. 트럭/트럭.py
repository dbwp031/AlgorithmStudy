import collections

n,w,L = map(int,input().split())
cars = list(map(int,input().split()))

q = collections.deque()

car_idx = 1
q.extend([0]*(w-1) + [cars[0]])

sec = 1

while q:
    # print(q)
    sec +=1
    node = q.popleft()

    if car_idx < len(cars):
        if sum(q) + cars[car_idx] <= L:
            q.append(cars[car_idx])
            car_idx +=1
        else:
            q.append(0)    
print(sec)
