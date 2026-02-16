import bisect

arr = [1,3,5,7,9]
print(bisect.bisect_left(arr, 0))
print(bisect.bisect_left(arr, 10))
print(bisect.bisect_right(arr, 0))