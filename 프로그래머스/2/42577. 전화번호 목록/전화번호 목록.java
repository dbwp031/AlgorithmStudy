import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Set<String> numbers = new HashSet<>(Arrays.asList(phone_book));
        
        for (String number: phone_book) {
            for(int end = 1; end < number.length(); end++) {
                String prefix = number.substring(0, end);
                if (numbers.contains(prefix)) {
                    return false;
                }
            }
        }
        return true;
    }
}