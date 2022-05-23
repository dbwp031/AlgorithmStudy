n = int(input())
board = list(map(int,input().split()))
m = int(input())

# dp는 테이블에서 해당 값이 무엇을 의미하는 지 정의하는 것이 1단계인 것 같다.
# 이번 문제에서는 현재 인덱스는 " 현재 위치에 기차의 끝이 있을 때의 최대 값"으로 설정했습니다.

# 처음에는 1줄 dp를 생각했다. 그런데 "현재 몇 개의 기차를 사용했는지"에 대한 정보가 필요했다.
# 그래서 1 줄 dp에 현재 기차의 값도 같이 저장할까 했지만, 그건 아닌것같아서 2차원 dp를 고려해봤고, 올바른 dp임을 확인했습니다.

# 이 문제를 풀면서, i<m일 때, 즉 일반 상태일 때의 점화식, 그렇지 않을 때(현재 인덱스가 m보다 작을때)로 나누느라 시간이 좀 걸렸습니다.
# 그리고 현재 인덱스는 "i개의 기차를 쓸 때, j번째 객실까지 포함해서의 최대값"입니다.
# 그리고, 현재 인덱스에서의 왼쪽과 위와도 비교해주면서(각각 화살표)를 통해서 각각 어떤 상황에 해당 값으로 업데이트를 하는지도 파악했습니다.
# 왼쪽 값으로 업데이트되는 것은 이번 인덱스에 기차를 설치하지 않고, 저번 인덱스의 최대값이 더 클때 입니다.
# 위에 값은, 현재 위치에서 기차를 사용하지 않았을 때가 더 클때입니다. 근데 지금 생각해보니, 같은 인덱스에서 기차가 더 많으면 당연히 더 높을수밖에
# 없어서 포함하지 않아도 될 듯 합니다.
# 그리고 dp[2][i-m] + sum(board[i-m:i]) =>은 현재 인덱스 j에 새로운 기차 끝이 추가될 때입니다.

# 이 문제를 풀면서 느낀건데 만약 dp문제로 판단이 되면, 적당한 dp테이블을 찾고, 점화식만 찾으면 구현은 그렇게 어렵지 않기 때문에(식이 정확할 때)
# 마음의 여유를 가지고 dp 테이블을 찾는게 중요할 것 같습니다.

dp = [[0]*(n+1) for _ in range(4)]
# if len(board)<=3:
#     print(sum(board))
# else:
# # 첫번째 줄
# for i in range(1,n+1):
#     if i<m:
#         dp[1][i]=max(sum(board[:i]),dp[1][i-1])
#     else:
#         dp[1][i]=max(sum(board[i-m:i]),dp[1][i-1])

# # 두번째 줄
# for i in range(3,n+1):
#     for k in range(1,m+1):
#         dp[2][i]=max(dp[1][i-k]+sum(board[i-k:i]),dp[2][i-1],dp[2][i])
#     # dp[2][i]=max(dp[1][i-m]+sum(board[i-m:i]),dp[2][i-1])

# for i in range(4,n+1):
#     for k in range(1,m+1):
#         dp[3][i]=max(dp[2][i-k]+sum(board[i-k:i]),dp[3][i-1],dp[3][i])

# 첫번째 줄
for i in range(1,n+1):
    if i<m:
        dp[1][i]=max(sum(board[:i]),dp[1][i-1])
    else:
        dp[1][i]=max(sum(board[i-m:i]),dp[1][i-1])

# 두번째 줄
for i in range(1,n+1):
    # dp[2][i]=max(dp[1][i-k]+sum(board[i-k:i]),dp[2][i-1],dp[2][i])
    if i>m:
        dp[2][i]=max(dp[1][i-m]+sum(board[i-m:i]),dp[2][i-1],dp[1][i])
    else:
        dp[2][i]=max(sum(board[:i]),dp[2][i-1])
for i in range(1,n+1):
    # dp[3][i]=max(dp[2][i-k]+sum(board[i-k:i]),dp[3][i-1],dp[3][i])
    if i>m:
        dp[3][i]=max(dp[2][i-m]+sum(board[i-m:i]),dp[3][i-1],dp[2][i])
    else:
        dp[3][i]=max(sum(board[:i]),dp[3][i-1])
# for d in dp:
#     print(*d)
print(max(dp[3]))