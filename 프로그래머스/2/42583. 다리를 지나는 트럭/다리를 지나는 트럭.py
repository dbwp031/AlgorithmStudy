from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    bridge = deque()  # (나가는 시간, 무게)
    time = 0
    cur_weight = 0
    
    while trucks:
        time += 1
        # 1. 현재 시간에 나갈 수 있는 트럭은 다 내보냄
        while bridge and bridge[0][0] <= time:
            t_out, t_w = bridge.popleft()
            cur_weight -= t_w
            
        # 2. 새 트럭이 들어올 수 있다면 진입
        if cur_weight + trucks[0] <= weight:
            new_w = trucks.popleft()
            cur_weight += new_w
            bridge.append((time + bridge_length, new_w))
        else:
            # 3. [핵심] 무게 때문에 못 들어오면, 맨 앞 트럭이 나가는 시간으로 점프!
            # 단, 'time'만 바꾸고 루프를 다시 돌려 위 'while bridge'에서 처리하게 함
            time = bridge[0][0] - 1 # 다음 루프 시작 시 time += 1이 되므로 -1 해줌
            
    # 마지막 트럭이 다리에 들어온 상태로 while문이 끝남
    # 마지막 트럭이 나가는 시간은 bridge의 맨 마지막 요소에 들어있음
    return bridge[-1][0]