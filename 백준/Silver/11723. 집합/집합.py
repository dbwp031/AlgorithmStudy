import sys
input = sys.stdin.readline
S = [0] * (21)
def solve(op, num):
    if op == "add":
        S[num] = 1
    elif op == "remove":
        S[num] = 0
    elif op == "check":
        print(S[num]) 
    elif op == "toggle":
        if S[num] == 0:
            S[num] = 1
        else:
            S[num] = 0
    elif op == "all":
        for i in range(1,21):
            S[i] = 1
    elif op == "empty":
        for i in range(1,21):
            S[i] = 0


M = int(input())
for _ in range(M):
    ops = input().split()
    op = ops[0]
    num = "-"
    if len(ops) == 2:
        num = int(ops[1])
    solve(op, num)    