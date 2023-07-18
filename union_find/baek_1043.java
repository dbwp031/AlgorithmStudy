package baek1043;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[] parent, partyNum;
    static boolean[] know;
    static boolean[][] parties;
    static int n,m;

    public static void main(String[] args) throws Exception{
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        parent = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            parent[i]=i;
        }
        know = new boolean[n + 1];
        Arrays.fill(know, false);
        parties = new boolean[m + 1][n + 1];
        for (int i = 1; i < m + 1; i++) {
            Arrays.fill(parties[i], false);
        }
        partyNum = new int[m + 1];
        Arrays.fill(partyNum, 0);
        st = new StringTokenizer(br.readLine());
        int numKnow = Integer.parseInt(st.nextToken());
        for (int i = 0; i < numKnow; i++) {
            int a = Integer.parseInt(st.nextToken());
            know[a] = true;
        }
        for (int i = 1; i < m + 1; i++) {
            st = new StringTokenizer(br.readLine());
            int numParty = Integer.parseInt(st.nextToken());
//            partyNum[i] = numParty;
            for (int j = 1; j < numParty + 1; j++) {
                int p = Integer.parseInt(st.nextToken());
                parties[i][p] = true;
            }
        }
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                for (int k = j; k < n + 1; k++) {
                    if(parties[i][j] && parties[i][k]) union_parent(j,k);
                }
            }
        }
        HashSet<Integer> firstKnowSet = new HashSet<>();
        for (int i = 1; i < n + 1; i++) {
            if(know[i]) firstKnowSet.add(i);
        }
        HashSet<Integer> knowSet = new HashSet<>();
        for (int k : firstKnowSet) {
            knowSet.add(find_parent(k));
        }
//        System.out.println(firstKnowSet.toString());
//        System.out.println("parent");
//        System.out.println(Arrays.toString(parent));
//        for (int i = 1; i < n + 1; i++) {
//            if (find_parent(i) == i && know[i]) {
//                knowSet.add(i);
//            }
//        }
//        System.out.println("knowSet "+knowSet.toString());
        for (int i = 1; i < n + 1; i++) {
            if (knowSet.contains(find_parent(i))) {
                know[i]=true;
            }
        }
        int answer = 0;
        for (int i = 1; i < m + 1; i++) {
            boolean canLie = true;
            for (int j = 1; j < n + 1; j++) {
                if (parties[i][j] && know[j]) {
                    canLie = false;
                }
            }
            if (canLie) {
                answer++;
            }
        }
//        for (boolean[] p : parties) {
//            System.out.println(Arrays.toString(p));
//        }
//        System.out.println("know");
//        System.out.println(Arrays.toString(know));
        System.out.println(answer);
    }

    private static void union_parent(int a, int b) {
        a = find_parent(a);
        b = find_parent(b);
        if(a<b) parent[b] = a;
        else parent[a] = b;
    }

    private static int find_parent(int a) {
        if(a==parent[a]) return a;
        return parent[a] = find_parent(parent[a]);
    }
}
