# 이 문제는 작은 코인이 큰 코인의 배수라는 조건이 없으면 그리디가 아닙니다.
# 그런데 그리디인걸 알고 푸니까 무지성 그리디로 시작해서 과연 도움이 될까 생각이 들긴 합니다...

import sys
input = sys.stdin.readline
n,k=map(int,input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
idx = -1
for i in range(n):
    if k//coin[i]==0:
        idx = i-1
        break
used = 0
while True:
    used += k//coin[idx]
    k %= coin[idx]
    idx-=1
    if idx == -1 or k == 0:
        break
print(used)