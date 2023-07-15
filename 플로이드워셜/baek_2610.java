package baek2610;

import java.io.*;
import java.util.*;

public class Main {
    static int INF = 100_000_000;
    static int[][] dist;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static int n,m;
    static int[] parent;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        dist = new int[n + 1][n + 1];
        parent = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            Arrays.fill(dist[i], INF);
        }

        for (int i = 1; i < n + 1; i++) {
            parent[i] = i;
            dist[i][i]=0;
        }

        for (int i = 1; i < m + 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            dist[s][e] = 1;
            dist[e][s] = 1;
            int p = Math.min(parent[s], parent[e]);
            parent[s]=p;
            parent[e]=p;

        }
        for (int i = 1; i < n + 1; i++) {
            for (int s = 1; s < n + 1; s++) {
                for (int t = 1; t < n + 1; t++) {
                    if (dist[s][t] > dist[s][i] + dist[i][t]) {
                        dist[s][t] = dist[s][i] + dist[i][t];
                        int p = Math.min(parent[s], Math.min(parent[i], parent[t]));
                        parent[s]=p;
                        parent[i]=p;
                        parent[t]=p;
                    }
                }
            }
        }

//        for (int i = 1; i < n + 1; i++) {
//            System.out.println(Arrays.toString(dist[i]));
//        }
        HashMap<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 1; i < n + 1; i++) {
            if (map.get(parent[i]) == null) {
                map.put(parent[i], new ArrayList<>());
                map.get(parent[i]).add(i);
            } else {
                map.get(parent[i]).add(i);
            }
        }
//        System.out.println(Arrays.toString(parent));
//        System.out.println(map.keySet());
        System.out.println(map.keySet().size());
        List<Integer> leaders = new ArrayList<>();
        for (Integer k : map.keySet()) {
            int leader = map.get(k).get(0);
            int minValue=INF;
            for (int i : map.get(k)) {
                int tempValue=0;
                for (int j = 1; j < n + 1; j++) {
                    if(dist[i][j]!=INF) tempValue = Math.max(tempValue, dist[i][j]);
                }
                if (tempValue < minValue) {
                    leader = i;
                    minValue = tempValue;
                }
            }
            leaders.add(leader);
//            System.out.println(leader);

        }
        Collections.sort(leaders);
        for (int l : leaders) {
            System.out.println(l);
        }
    }
}
