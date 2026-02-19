import sys
input = sys.stdin.readline

s,p = map(int,input().split())
dna = input().strip()
min_lst = list(map(int,input().split()))

idx_map = {"A": 0, "C": 1, "G": 2, "T": 3}
count = [0] * 4

def can_make_pwd():
    return all(count[i] >= min_lst[i] for i in range(4))

ans = 0
for i in range(len(dna)):
    count[idx_map[dna[i]]] += 1 # 새 문자 추가
    
    # 두번째 윈도우 시점. 가장 오래된 원소를 지운다.
    if i >= p:
        count[idx_map[dna[i-p]]] -= 1 # 오래된 문자 제거
    
    if i >= p-1: # 윈도우 완성 시점. 초기에는 쌓아나가다가 이 시점 이후로 계속해서 슬라이딩 윈도우 검사
        if can_make_pwd():
            ans += 1
print(ans)