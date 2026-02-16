# 일반 gravity
# EMPTY와 ITEM 2종류 존재
# 투포인터로 구현
# 각 컬럼단위로 하단부터 조회하며, write pointer를 둬서 item이 떨어질 위치를 관리
def standard_gravity():
    board = [
        [0,0,1,0,1],
        [1,0,1,1,1],
        [0,0,0,0,1],
        [0,1,1,1,1]
    ]
    # 0은 빈 공간, 1은 item

    EMPTY = 0
    ITEM = 1
    ROW_NUM = 4
    COL_NUM = 5

    for ci in range(COL_NUM):
        write = ROW_NUM - 1

        for ri in range(ROW_NUM-1, -1, -1):
            if board[ri][ci] == ITEM:
                board[ri][ci] = EMPTY
                board[write][ci] = ITEM
                write -= 1

    for b in board:
        print(b)

# wall gravity
# EMPTY, ITEM, WALL 3종류 존재
# WALL은 고정되어 있음
def wall_gravity():
    board = [
        [1,2,1,0,1],
        [0,1,2,1,0],
        [2,0,0,2,0],
        [0,0,2,1,2]
    ]
    # 0은 빈 공간, 1은 item

    EMPTY = 0
    ITEM = 1
    WALL = 2
    ROW_NUM = 4
    COL_NUM = 5

    for ci in range(COL_NUM):
        write = ROW_NUM - 1

        for ri in range(ROW_NUM-1, -1, -1):
            if board[ri][ci] == ITEM:
                board[ri][ci] = EMPTY
                board[write][ci] = ITEM
                write -= 1
            elif board[ri][ci] == WALL:
                write = ri - 1

    for b in board:
        print(b)

if __name__ == "__main__":
    wall_gravity()