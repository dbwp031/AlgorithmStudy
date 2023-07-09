import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N =  Integer.parseInt(br.readLine());
        int[] cost = new int[N + 1];
        int[] d = new int[N + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i < N+1; i++) {
            cost[i] = Integer.parseInt(st.nextToken());
        }

        // 1. 테이블 정의하기
        // d[i] = i번째 까지의 최고 수열 개수

        // 2. 점화식 구하기
        // d[k] = d[1...k-1에서 cost[i] > cost[?]인 ?값들] + 1

        // 3. 초기값
        // d[1] = 1

        d[1] = 1;
        for (int i = 1; i < N + 1; i++) {
            int maxCount=0;
            for (int j = 1; j < i; j++) {
                if (cost[j] < cost[i]) {
                    maxCount = Math.max(d[j], maxCount);
                }
            }
            d[i] = maxCount +1;
        }
//        System.out.println(Arrays.toString(d));
        System.out.println(Arrays.stream(d).max().getAsInt());
    }
}
