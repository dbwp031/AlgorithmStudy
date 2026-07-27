import java.util.*;

class Solution {
    
    private Set<Integer> candidates;
    private boolean[] visited;
    private int n;
    public int solution(String numbers) {
        this.candidates = new HashSet<>();
        this.n = numbers.length();
        this.visited = new boolean[this.n];
        
        dfs(numbers, "");
        int count = 0;
        for(int cand: candidates) {
            if (isPrime(cand)){
                count++;                
            }
        }
        return count;
    }
    
    void dfs(String numbers, String cur) {
        if (!cur.isEmpty()) {
            candidates.add(Integer.parseInt(cur));            
        }
        
        if (cur.length() == n) {
            return;
        }
        
        for (int i=0; i<n; i++) {
            if (visited[i]) continue;
            
            visited[i] = true;
            dfs(numbers, cur + numbers.charAt(i));
            visited[i] = false;
        }
    }
    
    boolean isPrime(int num) {
        if (num < 2) {
            return false;
        }
        
        for (int i=2; i<num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
    
}