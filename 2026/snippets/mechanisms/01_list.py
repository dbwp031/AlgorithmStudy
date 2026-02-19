import sys

lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))


lst = []
for i in range(10):
    before = sys.getsizeof(lst)
    lst.append(i)
    after = sys.getsizeof(lst)
    print(f"len={len(lst)}, size={after} bytes", "← 재할당!" if before != after else "")