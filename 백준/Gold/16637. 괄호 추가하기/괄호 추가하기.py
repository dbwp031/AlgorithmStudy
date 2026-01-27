import sys
import collections

def calc(a, exp, b):
    a = int(a)
    b = int(b)
    if exp == "+":
        num = a + b
    elif exp == "-":
        num = a - b
    elif exp == "*":
        num = a * b
    return num

def calc_list(lst):
    if len(lst) == 0:
        print("ERROR")
        return
    result = int(lst[0])

    for i in range(1, len(lst), 2):
        # print(i)
        exp = lst[i]
        result = calc(result, exp, lst[i+1])
    return result

n = int(input())
data = list(input())
# print(data)
ans = calc_list(data)
for i in range(1, len(data), 2):
    q = collections.deque()
    q.append([i])
    while q:
        exp_indexes = set(q.popleft())
        # print(exp_indexes)
        transformed = []
        for j in range(len(data)):
            if j+1 in exp_indexes: # 괄호 exp면 계산하고 3개 -> 1개
                exp = data[j+1]
                num = calc(data[j], data[j+1], data[j+2])
                transformed.append(num)
            elif j in exp_indexes or j-1 in exp_indexes: # 
                continue
            else:
                transformed.append(data[j])
        # print(transformed)
        result = calc_list(transformed)
        # print(result)
        ans = max(result, ans)

        max_exp_index = max(exp_indexes)
        for j in range(max_exp_index + 4, len(data), 2):
            q.append(exp_indexes | {j,})
print(ans)