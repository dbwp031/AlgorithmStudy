# Sorting
[바킹독 정렬 설명](https://blog.encrypted.gg/1013)

제한 없으면 라이브러리 쓰자.
## Basic Sort
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

## Merge Sort <- 얘는 외워두자.
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

## Quick Sort
* 빠른 알고리즘
* 직접 구현해야 하면, quick sort 쓰지 말아라 (머지 소트 써라)
* pivot이라고 이름 붙은 원소 하나를 제자리로 보내는 작업
  * pivot의 왼 쪽에는 pivot값보다 작은 애들만, 오른쪽은 큰 애들만 있어야 된다.

**추가적인 공간이 필요하지 않다. (In-Place Sort) 배열 안에서 자리 바꿈만으로 처리된다.  cache hit rate가 높아서 속도가 빠르다.** 

 ![image](https://github.com/dbwp031/AlgorithmStudy/assets/65337423/20aa10d3-69a5-4e06-937d-c09409f702eb)

```java
package sorting;

import java.util.Arrays;

public class Quick {
    static int[] arr = {3, 2, 7, 116, 62, 235, 1, 23, 55, 77};
    static int n = 10;

    public static void main(String[] args) {
        quick_sort(0, n);
        System.out.println(Arrays.toString(arr));

    }

    private static void quick_sort(int st, int en) {
        if (en <= st + 1) return;
        int pivot = arr[st]; // 이번 피봇은 st인덱스
        int l = st + 1; //
        int r = en - 1;
        while (true) {
            while(l <= r && arr[l]<= pivot) l++; // 이 while 문을 돌고 나면 l = pivot보다 큰 값을 가지는 가장 왼쪽에 있는 idx
            while(l <= r && arr[r]> pivot) r--; // r = pivot보다 작은 값을 가지는 가장 오른쪽에 있는 idx
            if(l>r) break; // 만약에 이 조건문이 true면, pivot의 좌 우에 배치가 잘 되어 있는거임
            swap(l,r); // l(pivot보다 값이 큰)은  오른쪽으로, r(pivot보다 값이 작은)은 왼쪽으로 들어가야 하니깐 l,r 스왑
            // 
        }
        swap(st, r); 
        // l의 왼쪽에는 pivot보다 작은애들이, r의 오른쪽에는 pivot보다 큰 애들이 위치한다.
        // 그런데 r이 l보다 왼쪽에 있는 순간의 위치는 "r+1 ~ n까지의 idx에 pivot보다 큰 값만 있음을 보장"하는 idx이다.
        // 그러니까 pivot과 r의 위치를 바꿔주면 pivot의 위치가 고정이 된다.
        quick_sort(st, r);
        quick_sort(r + 1, en);
    }

    private static void swap(int l, int r) {

        int tmp = arr[l];
        arr[l] = arr[r];
        arr[r]= tmp;
    }
}
```

## Counting Sort
![image](https://github.com/dbwp031/AlgorithmStudy/assets/65337423/e16295f6-b655-4799-9be6-56a818a390e1)

제공된 수 개수: N  
수의 범위: 1 ~ K  
복잡도: O(N+K)  
## Radix Sort
Non-Comparison Sort: counting Sort, Radix Sort  
Comparison Sort: bubble, merge, quick  
![image](https://github.com/dbwp031/AlgorithmStudy/assets/65337423/3a872f3f-cb9a-4068-add6-932c23ea75b7)
![image](https://github.com/dbwp031/AlgorithmStudy/assets/65337423/22270834-d5c8-44b4-8532-0566e9b4bb24)
![image](https://github.com/dbwp031/AlgorithmStudy/assets/65337423/af29a407-5a3a-48de-b25c-88f84b6d726c)

각 숫자를 1의 자리 ~ N자리까지 정렬을 반복해서 최종 정렬하는 알고리즘

* 1의 자리수 기준으로 정렬
* 10의 자리수 기준으로 정렬 -> 같은 값은 뒤에 push -> 각 줄은 1, 10의 자리 수 정렬 확정
