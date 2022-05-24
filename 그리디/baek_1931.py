# 첫번째 드는 생각은 dp로 풀수있을까 생각했다.
# 그런데 조건을 보면 시간이 너무 커서 메모리 초과가 뜰 것이고, 그러면 가능한 것은 그리디일 것이라고 생각했습니다.

# 처음에는 end는 작은 순으로, start는 큰 순으로 정렬을 했습니다.
# 그런데 그렇게되면 [0,1],[1,1] 에 대해서 1,1을 먼저 처리해버려 0,1이 포함되지 않는 케이스가 존재합니다.
# end부터 처리하게 되면 결국 그날까지의 최대 count를 저장하는 것이기 때문에, 사실 start의 정렬 순서가 중요하다기 보단
# 이 같은날 시작하고 끝나는 회의를 포함하게 처리하는 방법을 고려해야 했습니다.

# 이 문제는 그리디에서 필수적으로 다루는 "task scheduling problem"이라고 합니다.
import sys
input = sys.stdin.readline

n = int(input())
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))
board.sort(key=lambda x: [x[1],x[0]])

count = 0
now = 0
for s,e in board:
    if s >=now:
        now = e
        count+=1
print(count)
