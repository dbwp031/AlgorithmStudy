# 이해가 잘 안돼서 알고리즘을 봤는데 "카탈란 수"라고 한다.
# 아이디어가 재밌고, 알아두면 언젠간 한 번은 써먹을 수 있을 것 같다.
# https://suhak.tistory.com/77

import sys
input = sys.stdin.readline
t = int(input())
MAX = int(1000000007)
for _ in range(t):
    n = int(input())
    if n%2==1:
        print(0)
        continue
    dp = [0]*2501
    dp[0]=1
    
    for i in range(1,n//2+1):
        for j in range(0,i):
            dp[i]+=(dp[j]*dp[i-1-j])%MAX
    print(dp[n//2]%MAX)