package baek11659;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    // 1. 테이블 정의: d[k] = k번째 까지의 sum 값
    // 2. 점화식: d[k] = d[k-1] + cost[k]
    // a ~ b 까지의 sum값: d[b] - d[a-1]
    // 초깃값
    // d[0] = 0
    // d[1] = cost[k]
    static long d[];
    static int cost[];
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        d = new long[n + 1];
        cost = new int[n+1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n + 1; i++) {
            cost[i] = Integer.parseInt(st.nextToken());
        }
        d[0] = 0;
        d[1] = cost[1];

        for (int i = 1; i < n + 1; i++) {
            d[i] = d[i - 1] + cost[i];
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            System.out.println(d[end]-d[start-1]);
        }
    }
}
