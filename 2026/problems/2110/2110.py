import bisect

n,c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()

def can_install(houses, dist, c):
    count = 1
    last_position = houses[0]

    for i in range(1, len(houses)):
        if houses[i] - last_position >= dist:
            count += 1
            last_position = houses[i]
            if count >= c:
                return True
    return False

left = 1
right = data[-1] - data[0]
answer = 0

while left <= right:
    mid = (left + right) // 2

    if can_install(data, mid, c):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)