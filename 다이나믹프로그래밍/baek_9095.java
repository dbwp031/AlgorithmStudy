
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int d[];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        //1. 테이블 정의하기
        // d[i] = 1,2,3으로 i를 표현하는 경우의 수
        d = new int[12];
        Arrays.fill(d, -1);

        //2. 점화식 세우기
        // d[k] = d[k-1] + (k-2)

        //3. 초기값
        d[1] = 1;
        d[2] = 2;
        d[3] = 4;

        for (int t = 0; t < T; t++) {
            int N = sc.nextInt();
            if (d[N] != -1) {
                System.out.println(d[N]);
            } else {
                for (int n = 1; n < N + 1; n++) {
                    if (d[n] != -1) {
                        continue;
                    }
                    d[n] = d[n - 1] + d[n - 2] + d[n - 3];
                }
                System.out.println(d[N]);
            }
        }

    }
}
