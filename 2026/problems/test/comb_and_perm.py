from itertools import permutations, combinations

data = [1,2,3,4,5]
n = 2
# permutation 순열 nPr

per = [item for item in permutations(data, n)]
comb = [item for item in combinations(data, n)]

print(len(per), len(comb))
print(per)
print (comb)

def build_combination(arr, n):
    result = []
    path = []

    def dfs(start):
        if len(path) == n:
            result.append(path[:])
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            dfs(i+1)
            path.pop()
    dfs(0)
    return result

print(build_combination([1,2,3,4,5],2))

def build_permutation(arr, n):
    used = [False] * len(arr)
    result = []
    path = []

    def dfs():
        if len(path) == n:
            result.append(path[:])
            return
        
        for i in range(len(arr)):
            if not used[i]:
                path.append(arr[i])
                used[i] = True
                dfs()
                used[i] = False
                path.pop()
    dfs()
    return result

print(build_permutation([1,2,3,4,5],2))
