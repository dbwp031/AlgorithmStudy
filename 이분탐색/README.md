# 이분 탐색
**정렬되어 있는 배열**에서 특정 데이터를 찾기 위해 모든 데이터를 순차적으로 확인하는 대신 **탐색 범위를 절반으로 줄여가며 찾는** 탐색 방법

단순 이분 탐색 구현 문제라면 쉽지만, 이분 탐색을 응용해야 하는 문제는 킬러 문제라 나온다.

## 알고리즘 직접 구현
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    static int n,m;
    static int[] data;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws Exception{
        n = Integer.parseInt(br.readLine());
        data = new int[n+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n+1; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(data, 1, n+1);
//        System.out.println(Arrays.toString(data));
        m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            System.out.println(binarySearch(Integer.parseInt(st.nextToken())));
        }
    }

    private static int binarySearch(int target) {
        int st = 1;
        int en = n;
        while (st <= en) {
            int mid = (st + en) / 2;
            if (target > data[mid]) {
                st = mid+1;
            } else if (target < data[mid]) {
                en = mid - 1;
            } else {
                return 1;
            }
        }
        return 0;
    }
}
```

## 표준 라이브러리 사용
`Arrays.binarysearch()`같은 경우에 target이 있을 경우 해당 인덱스를, 없을 경우 -(low+1)을 리턴한다. 즉 `0 미만: 못찾음, 0이상: 찾음` 이라고 받아드릴 수 있다. 

```java
package baek1920;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n,m;
    static int[] data;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws Exception{
        n = Integer.parseInt(br.readLine());
        data = new int[n+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n+1; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(data, 1, n+1);
        m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            int result = Arrays.binarySearch(data, 1, n + 1, Integer.parseInt(st.nextToken()));
            System.out.println(result > 0 ? 1 : 0);
        }
    }
}
```
