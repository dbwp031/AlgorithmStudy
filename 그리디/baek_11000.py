# import sys
# input = sys.stdin.readline

# n= int(input())
# board=[]
# for _ in range(n):
#     board.append(list(map(int,input().split())))
# board.sort(key=lambda x:[x[0],-x[1]])
# end_list = []
# end_list.append(board[0][-1])
# count = 1
# maxV = 1
# for i in range(1,n):
#     end_list.sort()
#     # print(end_list)
#     s,e = board[i]
#     if len(end_list)==0:
#         count+=1
#         end_list.append(e)
#     if s < end_list[0]:
#         count +=1
#         end_list.append(e)
#         maxV = max(count,maxV)
#     else:
#         # while len(end_list)!=0 and end_list[0] <= s:
#         end_list.pop(0)
#         count-=1
#         end_list.append(e)
# print(maxV)

import heapq
n = int(input())
board = []
for _ in range(n):
    s,e = map(int,input().split())
    board.append([s,e])
board.sort()

room = []
heapq.heappush(room,board[0][1])
for i in range(1,n):
    s,e = board[i]
    if s < room[0]:
        heapq.heappush(room,e)
    else:
        heapq.heappop(room)
        heapq.heappush(room,e)
print(len(room))