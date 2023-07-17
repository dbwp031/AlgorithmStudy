# 백트래킹 알고리즘
현재 상태에서 가능한 모든 후보군을 따라 들어가며 탐색하는 알고리즘

dfs가 일반적인 백트래킹 알고리즘의 예시이다. 재귀 구조를 잘 활용하여 문제를 해결해나가는 듯 하다.

## 백준 15649: n과 m (1)
```java
package baek15649;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    static int n,m;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws Exception{
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        boolean[] state =  new boolean[n+1];
        Arrays.fill(state,false);
        backTrack(state,  new Stack<>());
    }
    private static void backTrack(boolean[] state, Stack<Integer> stack) {
        if (stack.size() == m) {
            stack.forEach(s -> System.out.print(s+" "));
            System.out.println();
//            System.out.println();
            return;
        }


        for (int i = 1; i < n + 1; i++) {
            if(state[i]) continue;
            stack.push(i);
            state[i] = true;
            backTrack(state, stack);
            state[i]=false;
            stack.pop();
        }
    }
}
```

## 백준 9663: N-Queen
```java

```
