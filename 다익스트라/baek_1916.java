package baek1916;

import java.io.*;
import java.util.*;

class Node implements Comparable<Node> {
    int end, weight;
    public Node(int end, int weight) {
        this.end = end;
        this.weight = weight;
    }
    @Override
    public int compareTo(Node o) {
        return Integer.compare(weight,o.weight);
    }
}
public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int[] dist;
    private static int INF=100_000_000;
    private static List<Node>[] list;
    private static int n,m,startNode,endNode;
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        dist = new int[n + 1];
        Arrays.fill(dist, INF);

        list = new ArrayList[n+1];
        for (int i = 0; i < n + 1; i++) {
            list[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            list[start].add(new Node(end, weight));
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        startNode = Integer.parseInt(st.nextToken());
        endNode = Integer.parseInt(st.nextToken());

//        StringBuilder sb = new StringBuilder();
        dijkstra(startNode);
//        System.out.println(Arrays.toString(dist));
        System.out.println(dist[endNode]);

    }

    private static void dijkstra(int start) {
        PriorityQueue<Node> queue = new PriorityQueue<>();
        boolean[] visited = new boolean[n+1];
        Arrays.fill(visited, false);
        queue.add(new Node(start, 0));
        dist[start]=0;

        while (!queue.isEmpty()) {
            Node curNode = queue.poll();
            int cur = curNode.end;

            if(visited[cur]) continue;
            visited[cur]=true;

            for (Node node : list[cur]) { // cur: 현재 노드 인덱스 node: cur 위치에서 갈 수 있는 vertex를 node.end로 가직 ㅗ있는 Node
                if (dist[node.end] > dist[cur] + node.weight) {
                    dist[node.end] = dist[cur] + node.weight;
                    queue.add(new Node(node.end, dist[node.end]));
//                    System.out.println(Arrays.toString(dist));
                }
            }

        }
    }
}
