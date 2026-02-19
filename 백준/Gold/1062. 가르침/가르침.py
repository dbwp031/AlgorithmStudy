from itertools import combinations
import sys
input = sys.stdin.readline

def bit(x):
    return 1 << (ord(x) - ord('a'))

n,k = map(int,input().split())

base = bit('a') | bit('n') | bit('t') | bit('i') | bit('c')
words = []
cand_mask = 0
for _ in range(n):
    word_mask = 0
    for w in input().strip():
        word_mask |= bit(w)
    word_mask &= ~base
    cand_mask |= word_mask
    words.append(word_mask)

if k < 5:
    print(0)
    sys.exit()
need = k-5
cands = [i for i in range(26) if (cand_mask >> i) & 1]

if len(cands) <= need:
    print(n)
    sys.exit()

ans = 0
for comb in combinations(cands, need):
    learned = 0
    for c in comb:
        learned |= (1 << c)
    
    cnt = 0
    for word_mask in words:
        if (learned & word_mask) == word_mask:
            cnt += 1
    ans = max(ans, cnt)
print(ans)