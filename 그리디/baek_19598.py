import heapq
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

board.sort(key=lambda x:[x[0],x[1]])

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