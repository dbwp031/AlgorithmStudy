import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        int n = people.length;
        
        int left = 0;
        int right = n-1;
        
        // left==right인 경우 어떻게 해야하지?
        // left == right -> 아직 그 1명이 안탔음 -> 태워야함
        // left > right -> 다 탔음
        int need = 0;
        while (left <= right) {
            if (left == right) {
                need++;
                break;
            }
            
            if (people[left] + people[right]  <= limit) {
                left++;
            }
            need++;
            right--;
        }
        return need;
    }
}