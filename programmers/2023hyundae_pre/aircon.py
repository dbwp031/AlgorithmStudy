# https://school.programmers.co.kr/learn/courses/30/lessons/214289?language=python3#fn1

def solution(temperature, t1, t2, a, b, onboard):
    N = len(onboard)
    temperature +=10
    t1+=10
    t2+=10
    INF = int(10e4)
    dp = [[INF] * N for _ in range(51)]
    dp[temperature][0] = 0
    for i in range(N-1):
        for t in range(51):
            if dp[t][i]==INF: # cost 생략
                continue
            for dt in (1,0,-1): #상승, 하강, 유지
                nt = t + dt # 실내 온도에서 이동 가능한 온도들
                # 각 비용이 드는 상황을 세부적으로 나누어서 정리하면 아래처럼 구현할 수 있겠네 비용이 0인 케이스 / 비용이 a인 케이스 / b인 케이스
                # 경우의 수를 다 쪼개서 생각했네
                # 실외 / 실내 /킴or끔 2x2x2 8개의 케이스를 쪼개서 분석해서 조건문으로 잘 걸어준게 문제를 이해하는데 큰 도움이 되었을 것 같다.
                if nt == temperature: dc = 0 # 희망 온도가 실외온도와 같은 경우에 비용은 0
                elif nt == t: dc = b # 희망온도가 실외온도와 다르고, 희망온도가 현재온도일 경우에 비용 b 
                elif t < temperature and dt == 1: dc = 0 #실외온도가 현재온도보다 높고 온도 상승일 경우에 비용 0
                elif t > temperature and dt == -1: dc = 0
                else: dc = a
                
                if nt < 0 or nt > 50:
                    continue
                if (onboard[i+1] == 1) and (nt > t2 or nt < t1): # 승객이 탑승하고 온도가 범위 밖일 경우에 생략
                    continue
                dp[nt][i+1] = min(dp[nt][i+1], dp[t][i]+dc)
    answer = min(dp[i][-1] for i in range(51))
    return answer                   
