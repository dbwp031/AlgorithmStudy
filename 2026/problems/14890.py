def checkAvailable(row, rbridge):
    n = len(row)
    # 옆칸과 2칸 이상 차이가 한번이라도 존재하면 불가능
    for i in range(0, n-1):
        lr = row[i]
        rr = row[i+1]
        if abs(lr - rr) >= 2:
            return False, rbridge
    # 1칸 혹은 0칸 차이나는 경우
    for i in range(0, n-1):
        lr = row[i]
        rr = row[i+1]
        
        if lr == rr:
            continue    
        # 왼 < 오 (2 -> 3)인 경우, i, i-1에 다리를 놓아야 하고, i-2가 0이거나 왼 높이와 같아야함
        elif lr - rr == -1: 
            if i == 0 or i == 1:
                return False, rbridge
            if i == 2:
                if row[i-1] == lr and rbridge[i-1] == False and rbridge[i] == False:
                    rbridge[i-1] = True
                    rbridge[i] = True
                    continue
                else:
                    return False, rbridge
            else:
                if row[i-1] == lr and row[i-2] <= lr  and rbridge[i-1] == False and rbridge[i] == False:
                    rbridge[i-1] = True
                    rbridge[i] = True
                    continue
                else:
                    return False, rbridge
        # 왼 > 오 (3,2)
        else:
            if i == n-1 or i == n-2:
                return False, rbridge
            if i == n-3:
                if row[i+1] == rr and rbridge[i+1] == False and rbridge[i] == False:
                    rbridge[i+1] = True
                    rbridge[i+2] = True
                    continue
                else:
                    return False, rbridge
            else:
                if row[i+1] == rr and row[i+2] and row[i+3] <= rr and rbridge[i+1] == False and rbridge[i+2] == False:
                    rbridge[i+1] = True
                    rbridge[i+2] = True
                    continue
                else:
                    return False, rbridge
    return True, rbridge


N, L = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
bridge = [[False] * N for _ in range(N)]

answer = 0
for i in range(N):
    row = board[i]
    rbridge = bridge[i]
    # print(row, checkAvailable(row, rbridge))
    flag, rbridge = checkAvailable(row, rbridge)
    bridge[i] = rbridge
    if flag:
        answer +=1
for i in range(N):
    row = [b[i] for b in board]
    rbridge = [b[i] for b in bridge]
    # print(row, checkAvailable(row, rbridge))
    flag, rbridge = checkAvailable(row, rbridge)
    for j in range(N):
        bridge[j][i] = rbridge[j]

    if flag:
        answer +=1
print(answer)