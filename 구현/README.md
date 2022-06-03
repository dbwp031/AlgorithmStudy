# 구현
## ⭐재귀
- [홀수 홀릭 호석](https://github.com/dbwp031/YujeCodingTest/blob/main/%EA%B5%AC%ED%98%84/baek_20164.py)
```
재귀 함수에서 return을 쓴다는 것: 그 위치에서 끝내겠다는 것 + 반환해야 할 것이 있다는 것
=> 즉 최종 완성물의 결괏값(return 값)을 사용해 상위 함수에서 사용해야 하는 것.

재귀 함수에서 파라미터로 사용하는 것: 업데이트하는 값, 혹은 사용해야 하는 변수들
업데이트하는 방법을 잘 사용해야 한다. 이 문제에서는 odd_n이다.

재귀 함수에서 어떤 행동을 어떤 위치에서 해야하는지 잘 정해야 한다.
#1 어디서 숫자들을 합칠 것인지
#2 어디서 홀수 개수를 셀 것인지
#3 어디서 minV maxV를 업데이트할 것인지
```

- [ZOAC](https://github.com/dbwp031/YujeCodingTest/blob/main/%EA%B5%AC%ED%98%84/baek_16719.py)
```
문제의 핵심: 현재 상태에서 문자를 추가했을때, "추가한 결과 문자열"이 사전상 최소가 되어야 한다.
=> 저는 완전탐색으로 구현했습니다. 하지만 아래 아이디어를 생각한다면 재귀로 구현이 가능합니다.
=> 현재 상태에서 그 다음에 사전에 오는 문자열: 현재 상태 + 현재 문자열 뒤에 있는 단어
그러니깐 STARTLINK 에서
가장 처음은 A, 그 다음은 A뒤에 것들만 처리되는 ARTLINK가 된 후, A 앞인 ST에 대해서도 처리하면 됩니다.
문자열 + f()
f() + 문자열
을 해주면 됩니다.
```

## in 함수에 대하여
- [마법사 상어와 비바라기](https://github.com/dbwp031/YujeCodingTest/blob/main/%EA%B5%AC%ED%98%84/baek_21610.ipynb)
```
in 함수는 복잡도가 O(N)으로, 구현문제에서도 이로 인해 시간초과가 발생할 수 있습니다.
만약에 가능한 경우의 수가 한정되어 있고, 메모리상 구현이 가능하다면 visited 배열을 만들어 복잡도를 O(1)로 줄일 수 있습니다.
```
## 구현 & 시뮬레이션에서의 TIP
-[마법사 상어와 파이어볼](https://github.com/dbwp031/YujeCodingTest/blob/main/%EA%B5%AC%ED%98%84/baek_20056.py)
1. "0이 되면 지워진다."와 같은 표현이 있으면, 실제로 지울 것  
2. 모두 짝수 or 홀수인지 파악하는 것은 allEven 이라는 bool타입변수를 선언하고, odd가 나오면 allEven=False로 값 할당
```
if mess!=0:
    if allOdd or allEven:
        for g in range(4):
            new_board[i][j].append([mess,speed,allS[g]])
    else:
        for g in range(4):
            new_board[i][j].append([mess,speed,allD[g]])
else:
new_board[i][j]=board[i][j]
```
