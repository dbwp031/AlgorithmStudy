
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int d[][];
    static int cost[][];
    public static void main(String[] args) throws IOException {
        d = new int[1001][3];
        cost = new int[1001][3];
        // 1. 테이블 정의하기
        // d[i][j]: i번째 집이 j번째 색깔을 칠할 때, 1~i번째까지 집의 총합

        // 2. 점화식 구하기
        // d[i][j_A] = min(d[i][j_B], d[i][j_C]) + cost[i][j_A]

        BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));

        int houseNum = Integer.parseInt(br.readLine());

        for (int i = 1; i < houseNum+1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            cost[i][0] = Integer.parseInt(st.nextToken());
            cost[i][1] = Integer.parseInt(st.nextToken());
            cost[i][2] = Integer.parseInt(st.nextToken());
        }


        // 3. 초기값
        d[1][0] = cost[1][0];
        d[1][1] = cost[1][1];
        d[1][2] = cost[1][2];

        for (int i = 2; i < houseNum + 1; i++) {
            for (int j = 0; j < 3; j++) {
                d[i][j] = Math.min(d[i - 1][(j + 1) % 3], d[i - 1][(j + 2) % 3]) + cost[i][j];
            }
        }
        System.out.println(Math.min(d[houseNum][0], Math.min(d[houseNum][1],d[houseNum][2])));
    }
}
