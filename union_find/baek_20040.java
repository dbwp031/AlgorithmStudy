
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[] parent;
    static int n,m;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        parent = new int[n];
        for (int i=0;i<n;i++) parent[i]=i;

        int firstCycle=0;
        for (int i = 1; i < m + 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if (find_parent(a) == find_parent(b)) {
                firstCycle = i;
                break;
            }
            union_parent(a,b);
        }
        System.out.println(firstCycle);
    }

    private static void union_parent(int a, int b) {
        a = find_parent(a);
        b = find_parent(b);
        if (a<b) parent[b] = a;
        else parent[a]= b;
    }

    private static int find_parent(int a) {
        if(parent[a]==a) return a;
        return parent[a] = find_parent(parent[a]);
    }
}
