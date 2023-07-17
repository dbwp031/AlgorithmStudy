# 배낭 문제(Knapsack Problem)
두가지 버전이 있다.
* 분할 가능한 배낭 문제
* 0-1 배낭 문제

분할 가능한 배낭 문제는 greedy 알고리즘으로 해결한다. `무게당 가장 높은 가치를 가지는 물건`부터 차곡 차곡 넣어주면 된다.

0-1 배낭 문제는 백트레킹, DP로 해결한다.

## 분할 가능한 배낭 문제

## 0-1 배낭 문제
### DP (2차원)
12865 문제를 DP로 해결한 코드이다.
```java
package knapsack;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class zeroOneDP {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n, k;
    static int[] weights, values;
    static int[][] d;
    public static void main(String[] args) throws Exception{
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        weights = new int[n + 1];
        values = new int[n + 1];
        d = new int[n+1][k+1];
        for (int i = 0; i < n + 1; i++) {
            Arrays.fill(d[i], 0);
        }

        for (int i = 1; i < n + 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            weights[i] = a;
            values[i] = b;
        }
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < k + 1; j++) {
                if (j < weights[i]) {
                    d[i][j] = d[i - 1][j];
                } else {
                    d[i][j] = Math.max(d[i - 1][j], d[i - 1][j - weights[i]] + values[i]);
                }
            }
        }

        System.out.println(d[n][k]);

        for (int[] a : d) {
            System.out.println(Arrays.toString(a));
        }
    }
}
```
### DP (1차원)
2차원 코드를 1차원으로 축소한 알고리즘이다. 메모리 사용량이 N*K에서 K가 되기 때문에, 이 알고리즘으로 기억하고 있자.
```java
package knapsack;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class dp1d {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n, k;
    static int[] weights, values;
    static int[] d;
    public static void main(String[] args) throws Exception{
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        weights = new int[n + 1];
        values = new int[n + 1];
        d = new int[k+1];
        Arrays.fill(d, 0);

        for (int i = 1; i < n + 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            weights[i] = a;
            values[i] = b;
        }
        for (int i = 1; i < n + 1; i++) {
            for (int j = k; j > weights[i] - 1; j--) {
                d[j] = Math.max(d[j], d[j - weights[i]] + values[i]);
            }
        }

        System.out.println(d[k]);

//        for (int[] a : d) {
//            System.out.println(Arrays.toString(a));
//        }
    }
}
```
### 백트래킹
이 방식으로 12865번 문제를 풀면 시간초과가 난다. 이유는 최대 100개의 물건이 제시되기 때문에, 최악의 경우에는 복잡도가 O(2^100)이다.
```java
package baek12865_backTrack;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int n, k;
    static int[] weights, values,states;
    static int answer = 0;
    public static void main(String[] args) throws Exception{
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        weights = new int[n + 1];
        values = new int[n + 1];
        states = new int[n + 1];
        Arrays.fill(states, 0);
        for (int i = 1; i < n + 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            weights[i] = a;
            values[i] = b;
        }
        backTrack(1,0);
        System.out.println(answer);
    }

    private static void backTrack(int startIndex,int nowValue) {
//        System.out.println(nowValue);
//        System.out.println(Arrays.toString(states));
        answer = Math.max(nowValue, answer);
        for (int i = startIndex; i < n + 1; i++) {
            states[i]=1;
            if (promising()) {
                backTrack(i+1,  nowValue+values[i]);
            }
            states[i]=0;
        }
    }

    private static boolean promising() {
        int weight = 0;
        for (int i = 1; i < n + 1; i++) {
            if(states[i]==1) weight += weights[i];
        }
        return weight <= k;
    }
}
```
