# 깊이 우선 탐색 (DFS)
깊이 우선 탐색은 재귀함수 혹은 스택 자료구조를 사용하는 탐색 방법입니다.
**백트래킹**이 필요한 문제에서 사용되는 방법입니다.

### 1. 재귀 함수 구현에 관하여
재귀 함수를 사용하다보니, 고려해야 할 변수가 BFS보다 상대적으로 많은 것이 특징입니다.  
예를 들어 방문 전,후로 visited를 True,False로 업데이트를 계속 해주어야 하는지, 말아야 하는지  
방문 한 노드의 개수를 count한다고 했을 때, 이 count를 return 해줌으로써 업데이트를 해야할지 말아야 할지, 와 같이 고민할 사항이 좀 많습니다.  
일단 웬만한 **간단한 탐색**은 고려해야 할 사항도 적고 일반적으로 시간도 덜 쓰는 **BFS를 사용하는 것을 권장**합니다.  
하지만 어려운 DFS를 구현하기 위해선 이런 간단한 DFS를 **반드시** 구현할 줄 알아야합니다.  
[백준 1303번 문제](https://www.acmicpc.net/problem/1303)를 풀면서 BFS와 DFS를 구현했고, DFS에서 구현하는데 어려움이 있었습니다.  
[1303.py](https://github.com/dbwp031/YujeCodingTest/blob/main/%EA%B9%8A%EC%9D%B4%EC%9A%B0%EC%84%A0%ED%83%90%EC%83%89/baek_1303.py) 및 [1303-2.py](https://github.com/dbwp031/YujeCodingTest/blob/main/%EA%B9%8A%EC%9D%B4%EC%9A%B0%EC%84%A0%ED%83%90%EC%83%89/baek_1303-2.py)에 고민한 내용이 적혀있고, [1303-3-solved.py](https://github.com/dbwp031/YujeCodingTest/blob/main/%EA%B9%8A%EC%9D%B4%EC%9A%B0%EC%84%A0%ED%83%90%EC%83%89/baek_1303-3-solved.py)에 최종 정리한 내용이 작성되어 있습니다.

정리의 핵심 부분은 아래와 같습니다. 만약 읽었는데 기억이 잘 안나거나 이해가 안되면, 문제랑 코드를 다시 보도록 하자.
```
count를 return 해주는데, 이 업데이트 된 count가 다른 dfs에 들어가게 된다.
내가 평소에 하던 방법은 최대 count를 전역 변수에 따로 저장해주었다.
이 코드는 count라는 값을 return해준다.
(1) 만약 count를 return해서 이 count를 계속 업데이트를 해주면 탐색한 수가 계속 커짐. => 전체 개수 구하는거에 사용하면 됨.
(2) 만약에 count를 업데이트 하지 않으면, 다른 곳을 탐색하고 돌아와도 현재까지의 개수가 유지됨.
```
