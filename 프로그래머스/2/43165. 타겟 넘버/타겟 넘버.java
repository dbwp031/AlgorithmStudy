class Solution {
    int[] numbers;
    int target;
    int count;
    public int solution(int[] numbers, int target) {
        this.numbers = numbers;
        this.target = target;
        
        dfs(0,0);
        
        return count;
    }
    
    void dfs(int total_sum, int cur) {
        if (cur == numbers.length) {
            if (total_sum == target) {
                count++;
            }
            return;
        }
        int cur_number = numbers[cur];
        dfs(total_sum + cur_number, cur+1);
        dfs(total_sum - cur_number, cur+1);
    }
}