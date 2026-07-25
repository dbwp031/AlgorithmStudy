class Solution {
    public long solution(int n, int[] times) {
        int minTime = Integer.MAX_VALUE;
        for(int time: times) {
            minTime = Math.min(minTime, time);
        }
        
        long left = 0;
        long right = (long) minTime * n;
        
        while(left < right) {
            long mid = left + (right - left) / 2;
            
            long passNum = getPassNum(mid, times);
            if (passNum < (long) n) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        return left;
    }
    
    long getPassNum(long target, int[] times) {
        long passNum = 0;
        for (long time: times) {
            passNum += target / time;
        }
        
        return passNum;
    }
}