import sys
input = sys.stdin.readline

state = 0
m = int(input())
for _ in range(m):
    ops = input().split()
    op = ops[0]
    if op == "add":
        x = int(ops[1])
        state |= (1 << (x-1))
    elif op == "remove":
        x = int(ops[1])
        state &= (~(1<<(x-1)))
    elif op == "check":
        x = int(ops[1])
        print((state >> (x-1)) & 1)
    elif op == "toggle":
        x = int(ops[1])
        state ^= (1<<(x-1))
    elif op == "all":
        state = (1 << 20) - 1
    elif op == "empty":
        state = 0