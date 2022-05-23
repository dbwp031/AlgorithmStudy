# 이렇게 최소비용으로 거리를 이동하는 법은 가장 쉬운 것 같다.
# 구현상 약간 헷갈린 점은 있지만, 결국, 현재 위치에 대한 최소만 확정해나가서 마지막의 크기로 답을 알 수 있습니다.
n =int(input())
board = list(input())
INF = int(1e9)
dp = [INF]*n
dp[0]=0
tile =['B','O','J']
t = 0
for i in range(0,n):
    t = tile.index(board[i])
    t = (t+1)%3
    next_tile = tile[t]
    for j in range(i,n): 
        if board[j]==next_tile:
            dp[j]=min(dp[j],dp[i]+(j-i)**2)
# print(dp)
if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])