import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[][] map;
    static boolean[][] visited;
    static int[] dx = {0,-1,0,1};
    static int[] dy = {1,0,-1,0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        map = new int[n][n];
        visited = new boolean[n][n];

        for(int i=0;i<n;i++){
            String line = br.readLine();
            for (int j=0; j<n; j++){
                map[i][j] = line.charAt(j)-'0';
            }
        }

        List<Integer> sizes = new ArrayList<>();
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++) {
                if (map[i][j] == 1 && !visited[i][j]) {
                    sizes.add(bfs(i,j));
                }
            }
        }

        Collections.sort(sizes);

        StringBuilder sb = new StringBuilder();
        sb.append(sizes.size()).append('\n');
        for (int size:sizes) {
            sb.append(size).append('\n');
        }
        System.out.print(sb);
    }
    static int bfs(int sx, int sy) {
        Deque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{sx, sy});
        visited[sx][sy] = true;
        int count=0;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0], y = cur[1];
            count++;

            for (int d=0;d<4;d++){
                int nx = x + dx[d];
                int ny = y + dy[d];
                if (nx <0 || nx >= n || ny < 0 || ny >= n) {
                    continue;
                }
                if (visited[nx][ny] || map[nx][ny] == 0) {
                    continue;
                }
                visited[nx][ny] = true;
                q.offer(new int[]{nx,ny});
            }
        }
        return count;
    }
}
