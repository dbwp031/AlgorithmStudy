package baek_4198;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] value = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            value[i] = Integer.parseInt(br.readLine());
        }

        int[] cars = new int[n * 2+1];
        for (int i = 1; i < n + 1; i++) {
//            cars[i] = value[i];
//            cars[2 *n + 1 - i] =value[i];
            cars[n + 1 - i] = value[i];
            cars[n + i] = value[i];
        }
        cars[0]=0;
        int[] d = new int[2 * n + 1];
        Arrays.fill(d,1);
        for (int i = 1; i < 2 * n + 1; i++) {
            for (int j = 1; j < i; j++) {
                if (cars[i] < cars[j]) {
                    d[i] = Math.max(d[i], d[j] + 1);
                }
            }
        }
//        System.out.println(Arrays.toString(cars));
//        System.out.println(Arrays.toString(d));

        int maxNum = 0;
        for (int i = 1; i < 2 * n + 1; i++) {
            maxNum = Math.max(maxNum, d[i]);
        }
        System.out.println(maxNum);
    }
}
