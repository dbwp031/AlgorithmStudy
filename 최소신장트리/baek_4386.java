package back4386;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Node implements Comparable<Node> {
    int from, to;
    float cost;
    public Node(int from, int to, float cost) {
        this.from = from;
        this.to = to;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node o) {
        return Float.compare(this.cost, o.cost);
    }

}
public class Main {
    static int n;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static List<Node> nodeList;
    static int[] parent;
    public static void main(String[] args) throws Exception {
        n = Integer.parseInt(br.readLine());
        nodeList = new ArrayList<>();
        float[][] stars = new float[2][n + 1];
        for (int i = 1; i < n+1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            stars[0][i] =Float.parseFloat(st.nextToken());
            stars[1][i] =Float.parseFloat(st.nextToken());
        }
        parent = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            parent[i]=i;
        }
        for (int i = 1; i < n + 1; i++) {
            for (int j = i + 1; j < n + 1; j++) {
                nodeList.add(new Node(i,j, (float) Math.sqrt(Math.pow(stars[0][i]-stars[0][j],2)+
                                                             Math.pow(stars[1][i]-stars[1][j],2))));
            }
        }
        Collections.sort(nodeList);
        float answer = 0.0F;
        int cnt = 0;

        for (Node node : nodeList) {
            if (union(node.from, node.to)) {
//                System.out.println(node.cost);
                answer += node.cost;
                cnt += 1;
            }
            if (cnt ==  n - 1) {
                break;
            }
        }
        System.out.println(answer);
    }

    private static boolean union(int a, int b) {
        a = find(a);
        b = find(b);
        if(a==b) return false;
        else parent[a] = b;
        return true;
    }

    private static int find(int a) {
        if(parent[a]==a) return a;
        return parent[a] = find(parent[a]);
    }
}
