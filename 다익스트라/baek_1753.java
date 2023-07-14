package baek1753;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

class Node implements Comparable<Node> {
    int end, weight;

    public Node(int end, int weight) {
        this.end = end;
        this.weight = weight;
    }

    @Override
    public int compareTo(Node node) {
        return Integer.compare(weight, node.weight);
    }
}

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final int INF = 100_000_000;
    static int v,e,k;
    static List<Node>[] list;
    static int[] dist;

    public static void main(String[] args) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(br.readLine());
        list = new ArrayList[v + 1]; // list[i] = i번째 vertex와 연결되어 있는 edge의 도착 vertaex정보와 edge의 weight

        dist = new int[v + 1]; // 특정 vertex로부터 각 노드까지의 도착점

        Arrays.fill(dist, INF);
        for (int i = 1; i < v + 1; i++) {
            list[i] = new ArrayList<>();
        }
        for (int i = 1; i < e+1; i++) {
            st = new StringTokenizer(br.readLine());
            int start=Integer.parseInt(st.nextToken());
            int end=Integer.parseInt(st.nextToken());
            int weight=Integer.parseInt(st.nextToken());
            list[start].add(new Node(end, weight));

        }
        StringBuilder sb = new StringBuilder();
        dikstra(k);
        for (int i = 1; i <= v; i++) {
            if(dist[i]==INF) sb.append("INF\n");
            else sb.append(dist[i] + "\n");
        }
        bw.write(sb.toString());
        bw.close();
        br.close();
    }

    private static void dikstra(int start) {
        PriorityQueue<Node> queue = new PriorityQueue<>();
        // PriorityQueue를 사용하는 이유
        // offer(입력): O(logN)
        // peek(get) : O(1)
        // poll(반환): O(logN)
        // size :       O(1)
        // PriorityQueue 종류
        // 최소힙을 사용하는 priorityqueue: new PriorityQueue<>()
        // 최대힙을 사용하는 priorityqueue: new PriorityQeue<>(Collections.reverseOrder())

        // 다익스트라 알고리즘의 흐름
        // 현재 위치에서 최소 거리로 가는 애를 확정한다.
        // 현재 위치에서 나머지 애들도 거리를 비교해서 업데이트한다.
        // 그다음 최소 거리로 가는 애로를 현재 위치로 변경한다...
        // 이런 흐름 -> fifo이되, 거리가 작은 애가 우선순위가 높아야 한다.
        boolean[] check = new boolean[v + 1];
        queue.add(new Node(start, 0));
        dist[start] = 0;

        while (!queue.isEmpty()) {
            Node curNode = queue.poll();
            int cur = curNode.end;

            if(check[cur]==true) continue;
            check[cur] = true;

            for (Node node : list[cur]) {
                if (dist[node.end] > dist[cur] + node.weight) {
                    dist[node.end] = dist[cur]+ node.weight;
                    queue.add(new Node(node.end, dist[node.end]));
                }
            }
        }
    }
}
