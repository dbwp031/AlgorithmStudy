import java.util.*;

class Solution {
    public int[] solution(int[] sequence, int k) {
        int l = 0;
        int size = 0;
        
        List<Pair> result = new ArrayList<>();
        for(int r=0; r<sequence.length;r++) {
            size += sequence[r];
            while(size > k && l<=r) {
                size -= sequence[l];
                l++;
            }
            if (size == k) {
                result.add(new Pair(l, r));
            }
        }
        Collections.sort(result);
        return new int[]{result.get(0).s, result.get(0).e};
    }
    
    class Pair implements Comparable<Pair>{
        int s;
        int e;
        int size;
        
        Pair(int s, int e) {
            this.s = s;
            this.e = e;
            this.size = e-s+1;
        }
        
        @Override
        public int compareTo(Pair other) {
            return Integer.compare(this.size, other.size);
        }
    }
}