def solution(arr):
    answer = []
    l = 0
    for r in range(0, len(arr)):
        if arr[l] == arr[r]:
            continue
        answer.append(arr[l])
        l = r
    answer.append(arr[l])
    return answer