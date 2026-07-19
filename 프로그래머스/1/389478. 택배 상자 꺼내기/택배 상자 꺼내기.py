def solution(n, w, num):
    height = n // w
    if n % w != 0:
        height += 1
    
    # 세팅하기
    board = [[0] * w for _ in range(height)]
    r,c = 0,0
    cur = 1
    while cur <= n:
        board[r][c] = cur
        
        if r % 2 == 0 and c == w-1:
            r+= 1
        elif r % 2 == 1 and c == 0:
            r+= 1
        elif r % 2 == 0:
            c += 1
        elif r % 2 == 1:
            c -= 1
        cur += 1
    
    tr, tc = -1,-1
    for r in range(height):
        for c in range(w):
            if board[r][c] == num:
                tr, tc = r,c
    
    box = 1
    r = tr + 1
    while r < height:
        if board[r][tc] != 0:
            box +=1
        r += 1
    return box
        