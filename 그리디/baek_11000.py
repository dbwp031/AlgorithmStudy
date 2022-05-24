import sys
input = sys.stdin.readline

n= int(input())
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))
board.sort(key=lambda x:[x[1],x[0]])

now_course = 0
count = 0
answer = 0
for i in range(n):
    s,e = board[i]
    if s >= board[now_course][1]:
        now_course+=1
        count-=1
    elif s < board[now_course][1]:
        count+=1
        answer = max(answer,count)
print(answer)
        
        

