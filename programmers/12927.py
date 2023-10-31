def solution(n, works):
    # 야근 피로도 = 야근을 시작한 시점에서 각 일의 남은 작업량^2을 더한 값
    # 당연히 클 수록 많다.
    hours_count = [0] * 50001 # i시간 업무가 hours_count[i]개 있다
    for w in works:
        hours_count[w] +=1
    
    now = max(works) # 현재 진행해야 하는 업무 인덱스 (최대 시간의 업무를 하는게 최적)
    while(n>0 and now>0):
        if hours_count[now] == 0: now -=1 # 만약 해당 시간의 업무가 없다면 현재 위치를 1칸 낮춰보자
        else: # 해당 시간의 업무가 남아있다면
            hours_count[now] -= 1 # 업무를 진행해라.
            hours_count[now-1] += 1 # 진행한 업무는 1시간 줄어는다.
            n-=1 # 한 시간 업무 진행
    answer = 0
    print(hours_count)

    for i in range(len(hours_count)):
        answer += (i**2)*hours_count[i]
    return answer
        
