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
