package baek11779;

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
        return Integer.compare(this.weight, o.weight);
    }
}
public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static List<Node>[] list;
    private static int[] dist;
    private static int n,m,startNode, endNode;
    private static int INF = 100_000_000;
    private static int[] preNode;
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        list = new ArrayList[n + 1];
        dist = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            dist[i] = INF;
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

        dijkstra(startNode);
//        System.out.println(Arrays.toString(dist));
//        System.out.println(dist[endNode]);
//        System.out.println(Arrays.toString(preNode));
        int cur = endNode;
        int count = 1;

        Stack<Integer> stack = new Stack<>();
        while (cur != startNode) {
            stack.push(cur);
            cur = preNode[cur];
            count +=1;
        }
        stack.push(cur);


        System.out.println(dist[endNode]);
        System.out.println(count);
        while (!stack.isEmpty()) {
            System.out.print(stack.pop()+" ");
        }
    }

    private static void dijkstra(int startNode) {
        PriorityQueue<Node> queue = new PriorityQueue<>();
        boolean[] visited = new boolean[n + 1];
        Arrays.fill(visited, false);
        preNode = new int[n + 1];
        Arrays.fill(preNode, -1);
        queue.add(new Node(startNode, 0));
        preNode[startNode] = startNode;

        dist[startNode] = 0;
        while (!queue.isEmpty()) {
            Node curNode = queue.poll();
            int cur = curNode.end;

            if(visited[cur]) continue;
            visited[cur] = true;
            for (Node node : list[cur]) {
                if (dist[node.end] > dist[cur] + node.weight) {
                    dist[node.end] = dist[cur] + node.weight;
                    queue.add(new Node(node.end, dist[node.end]));
//                    System.out.println(Arrays.toString(dist));
//                    System.out.println(Arrays.toString(preNode));
                    preNode[node.end] = cur;
                }
            }
        }
    }
}
