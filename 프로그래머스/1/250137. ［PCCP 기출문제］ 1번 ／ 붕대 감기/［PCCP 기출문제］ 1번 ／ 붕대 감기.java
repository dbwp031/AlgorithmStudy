import java.util.*;

class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int consecuteHealCnt = 0;
        
        int addHealNeedCnt = bandage[0];
        int secHealPower = bandage[1];
        int addHeal = bandage[2];
        
        int cur = 0;
        int prev = 0;
        int curHealth = health;
        for (int[] attack: attacks) {
            
            prev = cur;
            cur = attack[0];
            int power = attack[1];
            
            int diff = cur - prev -1;
            int healCnt = diff;
            curHealth += healCnt * secHealPower;
            if (healCnt >= addHealNeedCnt) {
                curHealth += addHeal * (healCnt / addHealNeedCnt);
            }
            curHealth = curHealth > health ? health : curHealth;
            
            curHealth -= power;
            if (curHealth <= 0) {
                return -1;
            }
            // System.out.println(curHealth +":" + Arrays.toString(attack));
        }
        return curHealth;
    }
}