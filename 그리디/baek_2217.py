import sys
input = sys.stdin.readline

n = int(input())
w = 0
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()
for i in range(n):
    w = max(data[i]*(len(data)-i),w)
print(w)