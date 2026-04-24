class Solution {
    public int solution(int[][] sizes) {
        int curW = sizes[0][0];
        int curH = sizes[0][1];
        
        for (int i=1; i<sizes.length; i++) {
            int nxtW1 = Math.max(curW, sizes[i][0]);
            int nxtH1 = Math.max(curH, sizes[i][1]);
            int nxtSize1 = nxtW1 * nxtH1;
            
            int nxtW2 = Math.max(curW, sizes[i][1]);
            int nxtH2 = Math.max(curH, sizes[i][0]);
            int nxtSize2 = nxtW2 * nxtH2;
            
            if (nxtSize1 < nxtSize2) {
                curW = nxtW1;
                curH = nxtH1;
            } else {
                curW = nxtW2;
                curH = nxtH2;
            }
        }
        int answer = curW * curH;
        return answer;
    }
}