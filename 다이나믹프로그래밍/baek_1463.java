import java.util.Scanner;

public class Main {
    static int d[];
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        // 1. 테이블 정의하기: d[i] = i를 1로 만드는 최소 연산 횟수
        d = new int[N+1];
        // 2. 점화식
        /*
        d[k] = min(d[k/3],d[k/2],d[k-1]) +1 (단 k/3 -> 3으로 나누어질때, k/2 -> 2로 나누어질 때)
         */
        // 3. 초기값
        d[0] = 1;

        for (int i = 2; i < N + 1; i++) {
            d[i] = d[i - 1] + 1;
            if (i % 2 == 0) {
                d[i] = Math.min(d[i], d[i / 2] + 1);
            }
            if (i % 3 == 0) {
                d[i] = Math.min(d[i], d[i / 3] + 1);
            }
        }
        System.out.println(d[N]);
    }
}
