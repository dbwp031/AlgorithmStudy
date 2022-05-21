# 이건 하루종일 노가다 같은 느낌으로 생각하다가 결국에 dp 테이블 그리다가 점화식 비스무리한 걸 알아낸 느낌입니다.
# 점화식 비스무리한 형태가 나왔을 때, 이게 한줄 dp로 구현이 안되는데(될거같지만 어지러워질때) 너무 거기에 막혀있었던 것 같은 느낌입니다.
# 이것처럼 1,2,3 3줄로 풀어낼 수 있을때 메모리 제한이 괜찮다면 풀어헤쳐서 이해하기 쉽게 변형해주는것도 푸는데 도움이 되는 것 같습니다.
t = int(input())
dp=[[0,0,0] for _ in range(10001)]
dp[1]=[1,0,0]
dp[2]=[1,1,0]
dp[3]=[2,0,1]

for i in range(4,10001):
    dp[i][0]=sum(dp[i-1][0:])
    dp[i][1]=sum(dp[i-2][1:])
    dp[i][2]=sum(dp[i-3][2:])

for _ in range(t):
    k = int(input())
    print(sum(dp[k]))