# 내가 푼 코드
# 사실 굳이 재귀로 구현할 필요는 없었던 코드
# 완전 무식하게 짠 코드
# data = input()
# screen = [None]*len(data)

# def f():
#     global data
#     temp = []
#     for i in range(len(data)):
#         if data[i]=='*':
#             continue
#         now = ''
#         screen[i] = data[i]
#         for j in range(len(screen)):
#             if screen[j]!=None:
#                 now += screen[j]
#         temp.append([now,i])
#         screen[i]=None
#     temp.sort()
#     if len(temp)== 0:
#         return
#     fn,fp = temp[0]
#     screen[fp] = data[fp]
#     data = data[:fp]+'*'+data[fp+1:]
#     print(fn)
#     f()
# f()

S = list(input())
result = ['']*len(S)

def f(arr,start):
    print(result)
    if not arr:
        return
    _min = min(arr)
    idx = arr.index(_min)
    result[start+idx]=_min
    print("".join(result))
    f(arr[idx+1:],start+idx+1)
    f(arr[:idx],start)
f(S,0)