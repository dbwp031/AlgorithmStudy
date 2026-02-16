def solution(N,M,A):
    def is_complete(fish_count, store_count, M):
        caught_types = sum(1 for count in fish_count if count > 0)
        return caught_types + store_count >- M
    
    answer = float('inf')
    left = 0
    fish_count = [0] * (M+1)
    store_count = 0

    for right in range(N):
        if A[right] == -1:
            continue
        if A[right] == -2:
            store_count += 1
        else:
            fish_count[A[right]] += 1
        
    while is_complete(fish_count, store_count, M):
        answer = min(answer, right-left + 1)
    
        if A[left] == -2:
            store_count -= 1
        elif A[left] != -1:
            fish_count[A[left]] -= 1
        
        left += 1
    return answer if answer != float('inf') else -1