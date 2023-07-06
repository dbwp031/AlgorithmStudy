
import java.util.Arrays;
import java.util.Scanner;

import static java.util.Arrays.stream;

public class Main {
    static long d[];
    static long stair[];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int stairN = sc.nextInt();
        // 1. 테이블 정의: d[i] = i번째 계단을 밟을 때의 최대값
        // 2. 점화식: d[k] = max(d[k-2] + stair[k], d[k-3] + stair[k-1] + stair[k])
        d = new long[301];
        Arrays.fill(d,0);
        stair = new long[301];

        for (int n = 1; n < stairN + 1; n++) {
            long t = sc.nextLong();
            stair[n]=t;
        }

        d[1] = stair[1];
        d[2] = stair[1] + stair[2];
        d[3] = Math.max(stair[1] + stair[3], stair[2] + stair[3]);

        for (int n = 4; n < stairN+1; n++) {
            d[n] = Math.max(d[n - 2], d[n - 3] + stair[n - 1]) + stair[n];
        }

        System.out.println(d[stairN]);
    }
}
