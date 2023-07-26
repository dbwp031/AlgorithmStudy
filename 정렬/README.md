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

