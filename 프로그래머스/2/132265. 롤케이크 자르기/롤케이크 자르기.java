import java.util.*;

class Solution {
    public int solution(int[] topping) {
        Map<Integer, Integer> remains = new HashMap<>();
        
        for (int i=0; i<topping.length;i++) {
            remains.put(topping[i], remains.getOrDefault(topping[i], 0) + 1);
        }
                
        Set<Integer> leftTypes = new HashSet<>();
        int rightCnt = remains.size();
        
        int sameCnt = 0;
        for(int i=0; i<topping.length;i++) {
            leftTypes.add(topping[i]);
            int leftCnt = leftTypes.size();
            
            int remainTypeCnt = remains.get(topping[i]);
            if (remainTypeCnt <= 1) {
                remains.remove(topping[i]);
                rightCnt--;
            } else {
                remains.put(topping[i], remainTypeCnt-1);
            }
            
            if (leftCnt == rightCnt) {
                sameCnt++;
            }
        }

        return sameCnt;
    }
}