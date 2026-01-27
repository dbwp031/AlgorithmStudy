import sys
from collections import deque
input = sys.stdin.readline

n,w,L = map(int,input().split())
cars = deque(map(int, input().split())) # car를 뽑아서 쓸꺼라 deque로

bridge = deque([0]*w)
cur = 0 # 무게
sec = 0

while cars or cur > 0:
    sec += 1
    out = bridge.popleft()
    cur -= out

    if cars and cur + cars[0] <= L:
        x = cars.popleft()
        bridge.append(x)
        cur += x
    else:
        bridge.append(0)

print(sec)