import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    a0 = list(map(int, input().split()))
    a1 = list(map(int, input().split()))

    if n == 1:
        print(max(a0[0], a1[0]))
        continue

    up = [0] * n
    down = [0] * n
    none = [0] * n

    up[0] = a0[0]
    down[0] = a1[0]
    none[0] = 0

    for j in range(1, n):
        up[j] = max(down[j-1], none[j-1]) + a0[j]
        down[j] = max(up[j-1], none[j-1]) + a1[j]
        none[j] = max(up[j-1], down[j-1], none[j-1])

    print(max(up[-1], down[-1], none[-1]))