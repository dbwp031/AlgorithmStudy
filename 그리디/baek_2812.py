# n,k = map(int,input().split())
# data = list(map(int,input()))

# comN = k+1
# q = []
# head = -1

# while comN > 1:
#     start = head+1
#     maxV = -1
#     end = min(start+comN,n)
#     for i in range(start,end):
#         # print(i)
#         if maxV < data[i]:
#             maxV = data[i]
#             head = i
#     print(maxV,end='')
#     comN -= (head-start)
# if head < n-1:
#     for i in range(head+1,n):
#         print(data[i],end='')

# n,k = map(int,input().split())
# data = list(map(int,input()))
# start = 0
# while start<n-1:
#     for i in range(start,n-1):
#         print(i)
#         if data[i]<data[i+1]:
#             data[i]=-1
#         else:
#             start = i+1
#             break
# print(data)


n,k = map(int,input().split())
K = k
data = list(map(int,input()))

stack = []
for i in range(n):
    
    if len(stack)==0:
        stack.append(data[i])
        continue
    
    while len(stack) > 0 and stack[-1] < data[i] and k >0:
        stack.pop(-1)
        k-=1
    stack.append(data[i])

for i in range(n-K):
    print(stack[i],end='')