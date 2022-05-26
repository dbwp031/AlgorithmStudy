n,k = map(int,input().split())
board = list(map(int,input().split()))

diff = []
for i in range(n-1):
    # 차이 , 왼쪽 사람
    diff.append([board[i+1]-board[i],i])
diff.sort(key=lambda x:[-x[0]])

diff = diff[:k-1]
diff.sort(key = lambda x: x[1])

start = 0
answer = 0
for i in range(k):
    if i == k-1:
        last = n-1
    else:
        _, last = diff[i]
    # print(start,last)
    answer+= board[last]-board[start]
    start = last+1
print(answer)