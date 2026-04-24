class Solution {
    public int[] solution(int[] answers) {
        int[] result = new int[3];
        
        for (int i=0; i<answers.length; i++) {
            int ans = answers[i];
            
            if (ans % 5 == (i+1) % 5) {
                result[0]++;
            }
            
            if (i % 2 == 0 && ans == 2) {
                result[1]++;
            } else if (i % 2 == 1) {
                if ((i / 2) % 4 == 0 && ans == 1) {
                    result[1]++;
                } else if  ((i / 2) % 4 == 1 && ans == 3) {
                    result[1]++;
                }  else if  ((i / 2) % 4 == 2 && ans == 4) {
                    result[1]++;
                }  else if  ((i / 2) % 4 == 3 && ans == 5) {
                    result[1]++;
                } 
                // 1 -> 1 / 0
                // 3 -> 3 / 1
                // 5 -> 4 / 2
                // 6 -> 5 / 3
                // 9 -> 1 / 4
                // 11 -> 3 / 5
            }
            if ((i % 10 == 0 || i % 10 == 1) && ans == 3) {
                result[2]++;
            } else if ((i % 10 == 2 || i % 10 == 3) && ans == 1) {
                result[2]++;
            } else if ((i % 10 == 4 || i % 10 == 5) && ans == 2) {
                result[2]++;
            } else if ((i % 10 == 6 || i % 10 == 7) && ans == 4) {
                result[2]++;
            } else if ((i % 10 == 8 || i % 10 == 9) && ans == 5) {
                result[2]++;
            }
        }
        
        int maxResult = Math.max(Math.max(result[0], result[1]), result[2]);
        int cntMax = 0;
        for (int num : result) {
            if (num == maxResult) {
                cntMax++;
            }
        }
        
        int[] rank = new int[cntMax]; 
        int rankIndex = 0;
        for (int i=0; i<3; i++) {
            if (result[i] == maxResult) {
                rank[rankIndex] = i+1;
                rankIndex++;
            }
        }
        return rank;
    }
}