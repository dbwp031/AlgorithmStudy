data = [int(i) for i in list(input())]

zeroCnt = 0
oneCnt = 0

if data[0] == 0:
    zeroCnt = 1
else:
    oneCnt = 1

# 이전 값과 이번 값이 다르면 cnt + 1
for i in range(1, len(data)):
    prev = data[i-1]
    curr = data[i]
    
    if prev == curr:
        continue
    else:
        if curr == 0: zeroCnt += 1
        else: oneCnt += 1

print(min(zeroCnt, oneCnt))