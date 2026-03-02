import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int,input().split()))
answer = [0] * n
stack = []
# 역순으로 조회하여 감소하는 stack
for i in range(n-1,-1,-1):
    while stack and tower[stack[-1]] <= tower[i]:
        j = stack.pop()
        answer[j] = i + 1
    stack.append(i)
print(*answer)