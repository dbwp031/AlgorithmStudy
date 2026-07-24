import java.util.*;

class Solution {
    public int solution(int n, int[] tops) {
        int totalSize = 2*n+1;
        int[] dp = new int[totalSize];
        dp[0] = 1;
        if (isTop(1, tops)) {
            dp[1] = 3;
        } else {
            dp[1] = 2;
        }
        // System.out.println(Arrays.toString(dp));
        
        for (int i=2; i< totalSize; i++) {
            if (!isTop(i, tops)) {
                dp[i] = (dp[i-2] + dp[i-1]) % 10007;
            } else {
                dp[i] = (dp[i-2] + dp[i-1] * 2)  % 10007;
            }
        }
        // System.out.println(Arrays.toString(dp));

        return dp[totalSize-1];
        
    }
    static boolean isTop(int x, int[] tops) {
        if (x % 2 == 0) {
            return false;
        }
        x = (x-1) / 2;
        return tops[x] == 1;
    }
}