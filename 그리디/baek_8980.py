n,c=map(int,input()) # n: 마을 수 / c: 트럭 용량
m = int(input()) # m: 박스 정보 개수
data = []
for _ in range(m):
    data.append(list(map(int,input().split())))
data.sort(key=lambda x:[x[0],x[1],])