import java.util.*;

class Solution {
    class Pair implements Comparable<Pair> {
        long diff;
        long time;
        
        Pair(int d, int t) {
            this.diff = (long) d;
            this.time = (long) t;
        }
        
        @Override
        public int compareTo(Pair other) {
            int diffResult = Long.compare(this.diff, other.diff);
            
            if (diffResult != 0) {
                return diffResult;
            }
            
            return Long.compare(this.time, other.time);
        }
    }
    public int solution(int[] diffs, int[] times, long limit) {
        long left = 1;
        long right = 1;
        for (int dif : diffs) {
            right = Math.max(right, (long) dif);
        }
        
        Pair[] pairs = new Pair[diffs.length];
        for(int i=0;i<diffs.length; i++) {
            pairs[i] = new Pair(diffs[i], times[i]);
        }
        
        while (left < right) {
            long mid = left + (right - left) / 2;
            
            if (isAvailable(mid, limit, pairs)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        return (int) left;
    }
    
    boolean isAvailable(long mid, long limit, Pair[] pairs) {
        long total = 0;
        long timePrev = 0;
        
        for (int i=0; i<pairs.length; i++) {
            Pair pair = pairs[i];
            
            if (pair.diff > mid) {
                long wrongCnt = pair.diff - mid;
                total += wrongCnt * (timePrev + pair.time);
            }
            total += pair.time;
            timePrev = pair.time;
        }
        
        if (total > limit) {
            return false;
        }
        
        return true;
    }
}