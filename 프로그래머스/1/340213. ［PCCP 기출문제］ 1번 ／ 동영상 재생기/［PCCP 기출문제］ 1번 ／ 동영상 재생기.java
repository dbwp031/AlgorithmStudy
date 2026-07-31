import java.util.*;

class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        
        // System.out.println(getSec(video_len));
        // System.out.println(prev(getSec(video_len)));
        
        int cur = getSec(pos);
        int len = getSec(video_len);
        int opStart = getSec(op_start);
        int opEnd = getSec(op_end);
        
        for (String command: commands) {
            cur = checkAndMoveOpEnd(cur, opStart, opEnd);
            
            if (command.equals("prev")) {
                cur = prev(cur);
            } else {
                cur = next(cur, len);
            }
            
            // System.out.println(command + ":" + cur);
        }
        
        cur = checkAndMoveOpEnd(cur, opStart, opEnd);
        return toStr(cur);
    }
    
    int checkAndMoveOpEnd(int cur, int op_start, int op_end) {
        if (cur > op_end || cur < op_start) {
            return cur;
        }
        
        return op_end;
    }
    
    int next(int cur, int len) {
        return cur + 10 > len ? len : cur + 10;
    }
    
    int prev(int cur) {
        return cur >= 10 ? cur - 10 : 0;
    }
    
    int getSec(String timeStr) {
        String[] parsed = timeStr.split(":");
        
        int sec = 60 * Integer.parseInt(parsed[0]) + Integer.parseInt(parsed[1]);
        return sec;
    }
    
    String toStr(int sec) {
        int min = sec / 60;
        int remainSec = sec % 60;
        
        return String.format("%02d", min) + ":" + String.format("%02d", remainSec);
    }
}