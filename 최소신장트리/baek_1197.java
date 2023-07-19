package baek1197;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.StringTokenizer;

class Node implements Comparable<Node> {
    int from, to, cost;

    public Node(int from, int to, int cost) {
        this.from = from;
        this.to = to;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node o) {
        return Integer.compare(this.cost, o.cost);
    }
}
public class Main {
    static int v,e;
    static int[] parents;
    static ArrayList<Node> nodeList;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());

        parents = new int[v + 1];
        nodeList = new ArrayList<>();

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            nodeList.add(new Node(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }
        Collections.sort(nodeList);
        
        make();
        
        int sum = 0;
        int cnt = 0;
        for (Node n : nodeList) {
            if (union(n.from, n.to)) {
                sum+=n.cost;
                cnt++;
                if(cnt==e-1) break;
            }
        }
        System.out.println(sum);
        
    }

    private static boolean union(int from, int to) {
        from = find(from);
        to = find(to);
        if(from == to) return false;
        else parents[to] = from;
        return true;
    }

    private static int find(int v) {
        if(parents[v]==v) return v;
        else return parents[v] = find(parents[v]);
    }
    private static void make() {
        for (int i = 1; i < v + 1; i++) {
            parents[i]=i;
        }
    }
}
