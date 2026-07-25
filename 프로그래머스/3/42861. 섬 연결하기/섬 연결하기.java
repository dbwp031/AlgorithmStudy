import java.util.*;

class Solution {
    public int solution(int n, int[][] costs) {
        Arrays.sort(costs, (a,b) -> {
            return Integer.compare(a[2], b[2]);
        });
        
        // for (int[] i: costs) {
        // System.out.println(Arrays.toString(i));            
        // }
        int totalCost = 0;
        DSU dsu = new DSU(n);
        for(int i=0; i<costs.length; i++) {
            int from = costs[i][0];
            int to = costs[i][1];
            int cost = costs[i][2];
            
            int rootFrom = dsu.find(from);
            int rootTo = dsu.find(to);
            
            if (rootFrom == rootTo) {
                continue;
            }
            
            dsu.union(rootFrom, rootTo);
            totalCost += cost;
        }
        return totalCost;
    }
    class DSU {
        int[] parent;
        
        DSU(int n) {
            parent = new int[n];
            for(int i=0;i<n;i++) {
                parent[i] = i;
            }
        }
        int find(int x) {
            if(parent[x] == x) {
                return x;
            }
            
            return parent[x] = find(parent[x]);
        }
        
        void union(int a, int b) {
            int rootA = find(a);
            int rootB = find(b);
            
            if (rootA == rootB) {
                return;
            }
            
            if (rootA < rootB) {
                parent[rootB] = rootA;
            } else {
                parent[rootA] = rootB;
            }
            
            return;
            
        }
    }
}