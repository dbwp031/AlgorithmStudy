from itertools import combinations

def solution(n, q, ans):
    def check(nums):
        for i in range(len(q)):
            cnt = 0 
            for item in q[i]:
                if item in nums:
                    cnt += 1
            if cnt != ans[i]:
                return False
        return True
    
    comb = combinations(range(1,n+1), 5)
    answer = 0
    for c in comb:
        # print(c)
        if check(c):
            answer +=1
    
    return answer




