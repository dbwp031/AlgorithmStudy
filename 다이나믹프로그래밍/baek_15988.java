
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static long d[];
    static long MOD = 1000000009;
    public static void main(String[] args) {
         //1. 테이블 정의하기
        // d[i] = 1,2,3으로 i를 표현하는 경우의 수
        d = new long[1000001];
        Arrays.fill(d, -1);

        //2. 점화식 세우기
        // d[k] = d[k-1] + (k-2)

        //3. 초기값
        d[1] = 1;
        d[2] = 2;
        d[3] = 4;
        for (int n = 4; n < 1000000 + 1; n++) {
            d[n] = (d[n - 1] + d[n - 2] + d[n - 3])%MOD;
        }

        Scanner sc = new Scanner(System.in);
        long T = sc.nextLong();

        for (int t = 0; t < T; t++) {
            int N = sc.nextInt();
            System.out.println(d[N]);
        }

    }
}
