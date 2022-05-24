#B의 가장 큰 수에 A의 가장 작은 수로 짝을 맞춰주면 된다.
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort(reverse=True)

ans = 0
for i in range(n):
    ans += a[i]*b[i]
print(ans)