from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    total_weight = 0
    q = deque([0]*(bridge_length))
    # truck_weights = deque([w for w in truck_weights])
    t=0
    cur_weight = 0
    while q:
        cur_weight -= q.popleft()
        t += 1
        if truck_weights and cur_weight + truck_weights[0] <= weight:
            cur_truck = truck_weights.pop(0)
            cur_weight += cur_truck
            q.append(cur_truck)
        elif truck_weights:
            q.append(0)
        
        if cur_weight == 0 and not truck_weights:
            break
            
    return t