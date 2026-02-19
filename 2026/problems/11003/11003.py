from collections import deque
import sys
input = sys.stdin.readline

n,l = map(int,input().split())
nums = list(map(int,input().split()))


# sliding window를 하면서 현재 최솟값만 가지고 있으면 최소 원소가 슬라이딩 윈도우에서 벗어났을 때, 그 이후의 min 값을 찾을 수 없다.
# 현재 슬라이딩 윈도우 기준, 최솟값들의 정보를 가지고 있어야 한다.
# 최솟 값들의 정보(최솟 값의 index)가 정렬되어 있어야 한다. -> 조회 O(1 ~ logN)까지만 가능하기 때문에
        

# 단조 덱 아이디어
# 덱 안의 값이 항상 오름차순을 유지하도록 관리
# -> 덱의 맨 앞이 항상 현재 윈도우의 최솟값

# 새 값이 들어올 때:
# 덱 뒤에서부터 새 값보다 크거나 같은 값을 모두 제거
# -> 어짜피 새 값이 더 작고 더 오래 남으므로 최솟값이 될 수 없음
# -> while 문을 돌아서 복잡도가 N이라고 생각할 수 있으나, "분할상환 분석(Amortized Analysis)"에 따라
# 삽입횟수는 N번(원소마다 1회) 제거 횟수: N번 이하 (한 번 제거되면 다시 안 들어옴)라 전체 whiel문 실행 횟수는 N번 이하.
dq = deque()
result = []

for i, num in enumerate(nums):
    if dq and dq[0][1] < i-l+1:
        dq.popleft()
    
    # dq를 pop 하는 것이 시간 복잡도를 상수 값만큼 제거해주는 것이 아니라, N배로 줄여줌. (분할상환 방식이기 때문.)
    # 이번에 새로 들어온 값보다 작으면 모두 제거하니깐, "현재 최소"를 유지하면서도 현재 위치를 보장. 정렬도 보장.
    while dq and dq[-1][0] >= num:
        dq.pop()
    
    dq.append((num , i))
    result.append(dq[0][0])

print(*result)