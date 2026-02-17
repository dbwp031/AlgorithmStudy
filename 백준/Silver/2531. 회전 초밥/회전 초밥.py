import sys
input = sys.stdin.readline

n,d,k,c = map(int,input().split())
fishes = []
for _ in range(n):
    fishes.append(int(input()))

# 원형 테이블이기 때문에 전부 검사를 위하여 리스트 뒤에 값 추가
# window size가 4면 3개 추가
for i in range(k-1):
    fishes.append(fishes[i])
eats = [0] * (d+1)
eats[c] = 1

max_eat_types = -1
for i in range(len(fishes)):
    eats[fishes[i]] += 1

    if i >= k:
        eats[fishes[i-k]] -= 1
    
    if i >= k-1:
        eat_types = sum(x >= 1 for x in eats[1:])
        max_eat_types = max(max_eat_types, eat_types)
print(max_eat_types)
