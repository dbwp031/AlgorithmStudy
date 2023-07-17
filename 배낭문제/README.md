# 배낭 문제(Knapsack Problem)
두가지 버전이 있다.
* 분할 가능한 배낭 문제
* 0-1 배낭 문제

분할 가능한 배낭 문제는 greedy 알고리즘으로 해결한다. `무게당 가장 높은 가치를 가지는 물건`부터 차곡 차곡 넣어주면 된다.

0-1 배낭 문제는 백트레킹, DP로 해결한다.

## 분할 가능한 배낭 문제

## 0-1 배낭 문제
### DP
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
