import sys
input = sys.stdin.readline

def calc(a, op, b):
    if op == "+": return a + b
    if op == "-": return a - b
    return a * b

n = int(input().strip())
s = input().strip()

nums = list(map(int, s[0::2]))
ops = list(s[1::2])

if len(nums) == 1:
    print(nums[0])
    sys.exit(0)

ans = -2**31

# 계산 우선순위 없이 왼쪽부터 연산하다 보니까
# dfs 해서 (왼쪽, 대상 ops, 오른쪽) 으로 처리할 수 있는 거임
def dfs(i, res):
    global ans
    
    if i == len(ops):
        ans = max(ans, res)
        return
    
    # 1) 괄호 안치기
    dfs(i + 1, calc(res, ops[i], nums[i + 1]))
    # 2) 괄호 치기
    if i + 1 < len(ops):
        bracket  = calc(nums[i+1], ops[i+1], nums[i+2])
        dfs(i+2, calc(res,ops[i], bracket))

dfs(0, nums[0])
print(ans)