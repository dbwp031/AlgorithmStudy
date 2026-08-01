import java.util.*;

class Solution {
    public String[] solution(String[] orders, int[] course) {
        char[][] sortedOrders = new char[orders.length][];
        for(int i=0; i<orders.length; i++) {
            sortedOrders[i] = orders[i].toCharArray();
            Arrays.sort(sortedOrders[i]);
        // System.out.println(sortedOrders[i]);
        }
        
        List<String> answer = new ArrayList<>();
        
        for (int targetLength : course) {
            Map<String, Integer> counts = new HashMap<>();
            
            for(char[] menus: sortedOrders) {
                if (menus.length < targetLength) {
                    continue;
                }
                combine(menus,0,targetLength, new StringBuilder(), counts);
            }
            int maxCount = 0;
                
                for(int count: counts.values()) {
                    maxCount = Math.max(maxCount, count);
                }
                
                if (maxCount < 2) continue;
                for(Map.Entry<String, Integer> entry: counts.entrySet()) {
                    if (entry.getValue() == maxCount) {
                        answer.add(entry.getKey());
                    }
                }
        }

    Collections.sort(answer);
    return answer.toArray(new String[0]);
    }
    
    private void combine(
        char[] menus,
        int start,
        int targetLength,
        StringBuilder selected,
        Map<String, Integer> counts
    ) {
        if (selected.length() == targetLength) {
            String combination = selected.toString();
            
            counts.put(combination, counts.getOrDefault(combination, 0) + 1);
            return;
        }
        
        int need = targetLength - selected.length();
        
        for(int i = start; i<= menus.length - need; i++) {
            selected.append(menus[i]);
            
            combine(menus, i+1, targetLength, selected, counts);
            selected.deleteCharAt(selected.length() - 1);
        }
    }
}