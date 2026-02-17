s,p = map(int,input().split())
dna = input()
# ACGT
min_lst = list(map(int,input().split()))
count = [0] * 4

def get_idx(w):
    if w == "A":
        idx = 0
    elif w == "C":
        idx = 1
    elif w == "G":
        idx = 2
    elif w == "T":
        idx = 3
    return idx

def can_make_pwd():
    can_pwd = True
    for i in range(4):
        if count[i] < min_lst[i]:
            can_pwd = False
    return can_pwd

ans = 0
for i in range(0, p):
    idx = get_idx(dna[i])
    count[idx] += 1

if can_make_pwd():
    ans += 1

for i in range(1, len(dna)-p+1):
    new_idx = get_idx(dna[i+p-1])
    old_idx = get_idx(dna[i-1])
    count[new_idx] += 1
    count[old_idx] -= 1
    if can_make_pwd():
        ans += 1

print(ans)