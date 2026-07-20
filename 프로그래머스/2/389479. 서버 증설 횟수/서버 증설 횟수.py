def solution(players, m, k):
    def get_need(player, m):
        # 5명, m = 3이면 needs = 2 사람 // m += 1
        if player < m:
            return 0
        player -= (m-1)
        need = player // m
        if player % m != 0:
            need += 1
        return need
    
    n = len(players)
    # needs = 각 시각마다 필요한 서버의 수
    # servers = 각 시간대 별로 현재 기준 서버의 수 각 players를 조회하면서 서버가 증설되면 servers[시간대~+k] += 1
    # 그래서 그 시간대 조회했는데 수가 이미 크거나 같으면 패스 없으면 증설 횟수 +=1
    needs = [0] * n
    servers = [0] * n
    adds = [0] * n
    for i in range(n):
        needs[i] = get_need(players[i], m)
    
    add_cnt = 0
    for i in range(n):
        cur_server_cnt = servers[i]
        if cur_server_cnt >= needs[i]:
            continue
        cur_need = needs[i] - cur_server_cnt
        for j in range(i, min(i+k, n)):
            servers[j] += cur_need
        
        adds[i] = cur_need
    # print(servers)
    # print(needs)
    # print(adds)
    return sum(adds)