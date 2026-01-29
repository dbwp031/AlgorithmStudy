# DP 문제 접근 템플릿
## STEP 1. DP 상태 정의
dp에 들어갈 한 문장 정의
```python
dp[i] = i번째까지 고려했을 때의 최적값
dp[i][j] = i번째까지 고려했을 때 상태 j의 최적값
```
## STEP 2. 점화식 만들기
```python
dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
```
현재 상태가 어디에서 왔는지를 경우로 쪼개서 사용
DP는 결국
```python
dp[현재] = (이전 상태들) 중 최적 + (현재 선택 비용/가치)
```
의 형태
## STEP 3. 초기값
가장 작은 문제 직접 계산
```python
dp[0] = ...
dp[1] = ...
```
## STEP 4. 정답 위치
- dp[N]
- max(dp)
## STEP 5. 최적화
- 메모리 -> 슬라이딩 윈도우
- 시간 -> 상태 줄이기

# DP vs Greedy
### Q. 현재 최선이 미래에도 최선인가?
- Yes: Greedy
- No: DP

### Q. 나중 선택 때문에 손해 볼 수 있나?
- Yes: DP
- No: Greedy

### Q. 되돌릴 수 있나?
- Yes: DP
- No: Greedy

=> 지금 선택이 미래를 망칠 수 있으면 DP

# DP keyword
- "최대/최소"
- "경우의 수"
- "~까지 고려"
- "연속"
- "되돌릴 수 없음"