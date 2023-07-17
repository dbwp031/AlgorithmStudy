package baek20303_third;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int n,m,k;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static int[][] parent;
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        parent = new int[3][n+1];
        for (int i = 1; i < n + 1; i++) {
            parent[0][i]=i;
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n + 1; i++) {
            parent[1][i] = Integer.parseInt(st.nextToken());
            parent[2][i] = 1;
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            union_parent(a, b);
        }
//        System.out.println("parent");
//        for (int i = 0; i < 3; i++) {
//            System.out.println(Arrays.toString(parent[i]));
//        }
        int groupNum = 0;
        for (int i = 1; i < n + 1; i++) {
            if(i == parent[0][i]) groupNum++;
        }
        int[] weights = new int[groupNum + 1];
        int[] values = new int[groupNum + 1];
        int g = 1;
        for (int i = 1; i < n + 1; i++) {
            if (i == parent[0][i]) {
                values[g] = parent[1][i];
                weights[g] = parent[2][i];
                g += 1;
            }
        }
//        System.out.println("values");
//        System.out.println(Arrays.toString(values));
//        System.out.println("weights");
//        System.out.println(Arrays.toString(weights));
//
//        System.out.println("dp");
        int[] d = new int[k];
        for (int i = 1; i < groupNum + 1; i++) {
            for (int j = k - 1; j > weights[i]-1; j--) {
                d[j] = Math.max(d[j], d[j - weights[i]] + values[i]);
            }
//            System.out.println(Arrays.toString(d));
        }
        System.out.println(d[k-1]);
    }


    private static void union_parent(int a, int b) {
        a = find_parent(a);
        b = find_parent(b);
        if (a < b) {
            parent[0][b] = a;
            parent[1][a]+= parent[1][b];
            parent[2][a]+= parent[2][b];
        } else if (a>b) {
            parent[0][a] = b;
            parent[1][b]+= parent[1][a];
            parent[2][b]+= parent[2][a];

        } else {
            parent[0][a] = b;
        }
    }

    private static int find_parent(int a) {
        if(parent[0][a]==a) return a;
        parent[0][a] = find_parent(parent[0][a]);
        return parent[0][a];
    }
}
