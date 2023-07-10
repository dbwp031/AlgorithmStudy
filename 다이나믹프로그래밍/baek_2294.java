package baek2294;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int target = Integer.parseInt(st.nextToken());
        int[] d = new int[target + 1];
        int[] coins = new int[n+1];
        int upperBound=100_005;
        Arrays.fill(d, upperBound);
        d[0]=0;
        for (int i = 1; i < n + 1; i++) {
            int coin = Integer.parseInt(br.readLine());
            coins[i] = coin;
            if (coin <= target) {
                d[coin] = 1;
            }
        }

        for (int i = 1; i < target + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (i - coins[j] > 0) {
                    d[i]= Math.min(d[i],d[i-coins[j]]+1);
                }
            }
        }
//        System.out.println(Arrays.toString(d));
        if (d[target] == upperBound) {
            System.out.println(-1);
        } else {

            System.out.println(d[target]);

        }
    }
}
