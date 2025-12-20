from collections import deque

# group을 찾은 후, 터뜨림. 그 후에 group 수를 반환. (그룹 수가 0이면 종료 필요)
dx = [0,1,0,-1]
dy = [1,0,-1,0]
H,W = 12, 6
def pop_groups(board):
    # dfs로 group 조사 및 "."로 변환
    visited = [[False for _ in range(6)] for _ in range(12)]
    to_pop = []
    group_count = 0

    for r in range(12):
        for c in range(6):
            # 빈공간이거나, 방문한 노드는 건너뛰기
            if board[r][c] == "." or visited[r][c]:
                continue
            color = board[r][c]
            q = deque([(r,c)])
            visited[r][c] = True
            group = [(r, c)]

            while q:
                x, y = q.popleft()
                for di in range(4):
                    nx, ny = x + dx[di], y + dy[di]
                    if 0<=nx<H and 0<=ny<W:
                        if not visited[nx][ny] and board[nx][ny] == color:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                            group.append((nx,ny))
            if len(group) >= 4:
                group_count += 1
                to_pop.extend(group)
    
    for x, y in to_pop:
        board[x][y] = "."
    
    return group_count
    
def gravity(board):
    for i in range(6):
        line = [row[i] for row in board]
        colors = [item for item in line if item != "."]

        for c in range(12):
            board[c][i] = "."
        
        for j in range(len(colors)):
            row_index = 12 - len(colors) + j 
            # print(row_index, j)
            board[row_index][i] = colors[j]
    # print("====gravity====")
    # for l in board:
    #     print(l)
    return board

# # board를 중력 처리 한 후 board를 반환.
# def gravity(board):
#     # 각 열 별로, top item과 top -1 item을 찾은 후, top을 top -1 item 바로 위로 이동시킴.
#     for i in range(6):
#         top_row_index = find_index(board, i, 1)
#         top2_row_index = find_index(board, i, 2)
        
#         # row에 데이터가 0개인 경우, 넘어간다.
#         if top_row_index == -1: 
#             continue
#         # row에 데이터가 1개인 경우, top을 0으로 내린다.
#         if top2_row_index == -1:
#             board[0][i] = board[top_row_index][i]
#             board[top_row_index][i] = "."
#             continue
#         # 그 외
#         if top_row_index != -1 and top2_row_index != -1:
#             board[top2_row_index + 1][i] = board[top_row_index][i]
#             board[top_row_index][i] = "."
#             continue
#         print("[DEBUG] gravity 예상 외 예외 발생!!!")
#         print(i, top_row_index, top2_row_index)
#     print("====gravity====")
#     for l in board:
#         print(l)
#     return board

# # 특정 row의 topN번째 데이터의 rowIndex를 반환한다. 
# def find_index(board, row_index, topN):
#     # row_index 열 데이터
#     line = [row[row_index] for row in board]
#     count = 0
#     for i in range(len(line)):
#         if i == ".":
#             count += 1
#         if count == topN:
#             return i
#     return -1


################################

# 1. board 입력 받기
board = []
for _ in range(12):
    board.append(list(input()))
# for l in board:
#     print(l)

cycle = 0
while True:
    group_count = pop_groups(board)
    if group_count == 0:
        break
    board = gravity(board)
    cycle += 1

print(cycle)