// package baek1495;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;
/*
내가 푼 방법은 j-now >0이면 d[j-now]=now의 index값을 넣어주는 방식으로 dp를 구현했다.
이렇게 for문을 통해 배열을 접근하면서, for문 내에서 배열의 값을 변경하면 에러가 발생할 수 있다.
이 문제에서도 이 사항을 고려하지 않으면 틀린다.

나는 queue를 사용해서 for문을 다 돈 후에 한번에 업데이트 하는 방법으로 문제를 해결했다.

또 다른 방법은 2차원 배열을 사용해 해결하는 법이다.
https://mygumi.tistory.com/145
*/
public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        Queue<Integer> queue = new LinkedList<>();
        int[] d = new int[1001];
        Arrays.fill(d,-1);
        d[s] = 0;
        st = new StringTokenizer(br.readLine());

        boolean canLast = true;
        for (int i = 1; i < n + 1; i++) {
            int now = Integer.parseInt(st.nextToken());
            for (int j = 0; j < 1001; j++) {
                if (d[j] == i - 1) {
                    if (j - now >= 0) {
//                        d[j - now] = i;
                        queue.add(j - now);
                    }

                    if (j + now <= m) {
//                        d[j + now] = i;
                        queue.add(j + now);
                    }
                }
            }
            while (!queue.isEmpty()) {
                int item = queue.poll();
                d[item] = i;
            }
        }
        int maxVolume = -1;
        for (int i = 0; i < m + 1; i++) {
            if(d[i]==n) maxVolume = i;
        }
        // System.out.println(Arrays.toString(d));
        System.out.println(maxVolume);
    }
}
