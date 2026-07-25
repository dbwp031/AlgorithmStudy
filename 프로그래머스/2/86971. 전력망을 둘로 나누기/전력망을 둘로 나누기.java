import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = -1;
        
        int minSize = Integer.MAX_VALUE;
        for (int i=0; i<wires.length; i++) {
            DSU dsu = new DSU(n);
            
            for (int j=0; j<wires.length; j++) {
                if (j==i) {
                    continue;
                }
                dsu.union(wires[j][0],wires[j][1]);
            }
            
            // System.out.println(Arrays.toString(dsu.parent));
            // System.out.println(Arrays.toString(dsu.size));
            int left = dsu.find(wires[i][0]);
            int right = dsu.find(wires[i][1]);
            minSize = Math.min(Math.abs(dsu.size[left]-dsu.size[right]), minSize);
            // System.out.println(left + " " + right + " " + minSize);
        }
        return minSize;
    }
    
    class DSU {
        int[] parent;
        int[] size;
        
        DSU(int n) {
            parent = new int[n+1];
            size = new int[n+1];
            
            for(int i=1;i<n+1;i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }
        
        int find(int x) {
            if (parent[x] == x) {
                return x;
            }
            
            return parent[x] = find(parent[x]);
        }
        
        void union(int a, int b) {
            int rootA = find(a);
            int rootB = find(b);
            
            if (rootA < rootB) {
                parent[rootB] = rootA;
                size[rootA] += size[rootB];
            } else {
                parent[rootA] = rootB;
                size[rootB] += size[rootA];
            }
            return;
        }
    }
}