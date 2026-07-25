import java.util.*;

class Solution {
    
    public int solution(String[] want, int[] number, String[] discount) {
        Map<String, Integer> needs = new HashMap<>();
        Map<String, Integer> buys = new HashMap<>();
        for(int i=0;i<want.length;i++) {
            needs.put(want[i], needs.getOrDefault(want[i], 0) + number[i]);
        }
        int dayCnt = 0;
        for(int r=0;r<discount.length; r++) {
            // r번째에서는 r의 buys를 1 키움
            
            buys.put(discount[r], buys.getOrDefault(discount[r], 0) + 1);
            // buys.get(discount[r])++;
            if (r < 9) {
                continue;
            }
            // 딱 10일 되는 날에는 검토만 한다.
//             if (r == 9) {
                
//             }
            
            if (r >= 10) {
                buys.put(discount[r-10], buys.get(discount[r-10])-1);
            }
            
            if (canBuy(needs, buys)) {
                
                // System.out.println("BUY!!");
                dayCnt++;
            }
        }
        return dayCnt;
    }
    
    boolean canBuy(Map<String, Integer> needs, Map<String, Integer> buys) {
        // System.out.println(needs);
        // System.out.println(buys);
        // System.out.println("=====");
        for (Map.Entry<String, Integer> need: needs.entrySet()) {
            String item = need.getKey();
            int needCnt = need.getValue();
            int buyCnt = buys.get(item) == null ? 0 : buys.get(item);
            
            if (buyCnt < needCnt) {
                return false;
            }
        }
        return true;
    }
}