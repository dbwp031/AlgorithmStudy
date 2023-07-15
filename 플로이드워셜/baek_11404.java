package baek11404;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int m;
    static int[][] dist;
    static int INF = 100_000_000;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        dist = new int[n + 1][n + 1];
        for (int i = 0; i < n + 1; i++) {
            Arrays.fill(dist[i], INF);
        }

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            if(dist[start][end]>weight) dist[start][end]=weight;
        }

        // 플로이드 워셜
        for (int i = 1; i < n + 1; i++) {
            for (int s = 1; s < n + 1; s++) {
                for (int t = 1; t < n + 1; t++) {
                    if (dist[s][t] > dist[s][i] + dist[i][t]) {
                        dist[s][t] = dist[s][i] + dist[i][t];
                    }
                }
            }
        }
        for (int i = 1; i < n + 1; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 1; j < n + 1; j++) {
                if(i==j) sb.append("0 ");
                else if(dist[i][j]==INF) sb.append("0 ");
                else sb.append(dist[i][j] + " ");
            }
            System.out.println(sb);
        }
    }
}
