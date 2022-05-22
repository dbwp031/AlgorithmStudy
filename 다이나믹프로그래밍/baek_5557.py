# 이문제는 기타 문제랑 많이 비슷한 것 같습니다.
# 구현은 매우 쉽게 성공했는데,
# 인덱스 1씩 밀리거나, 당겨지는 식으로 구현해서 조금 헤맸습니다.
# dp에서 인덱스를 설정할 때, "현재 이 인덱스를 접근할 때, 이 인덱스 값들을 최적화 시키는 것인지, 이 인덱스 값들이 최적화되어 있는 것인지"
# 를 확인하고 구현하는게 좋을 것 같습니다.
n = int(input())
data = list(map(int,input().split()))

dp = [[0]*(21) for _ in range(n)]
dp[0][data[0]]=1
for i in range(1,n-1):
    for j in range(0,21):
        if dp[i-1][j]>=1:
            if j - data[i] >= 0:
                dp[i][j-data[i]] += dp[i-1][j]
            if j + data[i] <=20:
                dp[i][j+data[i]] += dp[i-1][j]

# for d in dp:
#     print(*d)

print(dp[n-2][data[-1]])