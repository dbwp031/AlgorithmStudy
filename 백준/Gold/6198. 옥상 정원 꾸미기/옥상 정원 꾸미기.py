import sys
input = sys.stdin.readline

n = int(input())
height = []
for _ in range(n):
    height.append(int(input()))

# 내려가는거
stack = []

h = 0
for i in range(n):
    # print(stack)
    while stack and height[stack[-1]] <= height[i]:
        stack.pop()
    h += len(stack)
    stack.append(i)

print(h)