import sys
input = sys.stdin.readline

N,K = map(int,input().split())

dp = [0] * (K+1)

for _ in range(N):
    w, v = map(int,input().split())

    # 최대 한도부터 물건 무게까지
    for j in range(K,w-1,-1):
            cand = dp[j-w] + v
            if cand > dp[j]:
                dp[j] = cand

print(dp[K])