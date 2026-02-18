def solution(schedules, timelogs, startday):
    def get_realtime(time):
        hour, min = time // 100, time % 100
        return hour * 60 + min
    
    answer = 0
    for i in range(len(schedules)):
        schedule = schedules[i]
        timelog = []
        for j in range(7):
            now = (startday-1+j) % 7
            if now in [5,6]:
                continue
            timelog.append(timelogs[i][j])
        print(timelog)
        is_success = all(get_realtime(time) <= get_realtime(schedule) + 10 for time in timelog)
        if is_success:
            answer += 1
    return answer