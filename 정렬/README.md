# 정렬
[바킹독 정렬 설명](https://blog.encrypted.gg/1013)
## 기초 정렬
O(N^2)
```java
package sorting;

import java.util.Arrays;

public class basic {
    static int[] arr = {3, 2, 7, 116, 62, 235, 1, 23, 55, 77};
    static int n = 10;

    public static void main(String[] args) {
        int count = 0;
        for (int i = n - 1; i > 0; i--) {
            int maxIdx = 0;
            for (int j = 1; j <= i; j++) {
                count++;
                if (arr[j] > arr[maxIdx]) maxIdx = j;
            }
            int temp = arr[i];
            arr[i] = arr[maxIdx];
            arr[maxIdx] = temp;
        }
        System.out.println(Arrays.toString(arr));
        System.out.println(count);
    }
}
```

## merge sort
![image](https://github.com/dbwp031/AlgorithmStudy/assets/65337423/c87a20e7-35de-43b0-b676-82acc5137be7)

O(NlogN)
재귀를 사용하여 병합 정렬

```java
package sorting;

import java.util.Arrays;

public class Merge {
    static int[] arr = {3, 2, 7, 116, 62, 235, 1, 23, 55, 77};
    static int[] temp = new int[10];
    static int n = 10;

    public static void main(String[] args) {
        merge_sort(0, n);
        System.out.println(Arrays.toString(arr));
    }

    private static void merge_sort(int st, int en) {
        if(en == st+1) return;
        int mid = (st+en)/2;
        merge_sort(st, mid);
        merge_sort(mid, en);
        merge(st, en);
    }

    private static void merge(int st, int en) {
        int mid = (st + en)/2;
        int lidx = st; // 왼쪽 블록의 첫 인덱스 (왼쪽 블록은 정렬된 상태)
        int ridx = mid; // 오른쪽 블록의 첫 인덱스 * 오른쪽 블록은 정렬된 상태)
        for (int i = st; i < en; i++) {
            if(ridx == en) temp[i] = arr[lidx++]; // 오른쪽 블록 끝까지 찾았다면 왼쪽 블록을 차근 차근 넣어라.
            else if (lidx == mid) temp[i] = arr[ridx++]; // 왼쪽 블록을 끝까지 찾았다면 오른쪽 블록을 차근 차근 넣어라.
            else if (arr[lidx]<=arr[ridx]) temp[i] = arr[lidx++]; // 왼쪽 블록 값이 오른쪽 블록 값보다 작다면 왼쪽값을 넣어라.
            else temp[i] = arr[ridx++]; // 반대면 오른쪽 값을 넣어라.
        }
        for (int i = st; i < en; i++) arr[i] = temp[i];
    }
}
```

