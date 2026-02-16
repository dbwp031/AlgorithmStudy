def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))
    m = int(input())
    inputs = list(map(int, input().split()))

    data.sort()
    for i in inputs:
        out = binary_search(data, i)
        if out == -1:
            print(0)
        else:
            print(1)