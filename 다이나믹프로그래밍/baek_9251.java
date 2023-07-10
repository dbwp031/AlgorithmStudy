package baek9251;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s1 = br.readLine();
        String s2 = br.readLine();
        // 1. 테이블 정의하기
        // d[i][j] = s2의 i번째 index까지와 s1의 j번째 index까지 비교했을 때의 최대 길이 크기
        // 2. 점화식
        // d[i][j] = max(d[i-1][j],d[i][j-1], 만약 s1[j] == s2[i]라면, d[i-1][j-1]+1)
        // s1[j] == s2[i]이면 각자 1개씩 이전의 최선의 값 + 이번에 겹침으로써 1이 더해짐
        // 3. 초기값
        // 0번째 인덱스 0
        int[][] d = new int[s2.length()+1][s1.length()+1];
        
        for (int i = 0; i < s2.length() + 1; i++) {
            for (int j = 0; j < s1.length() + 1; j++) {
                if (i == 0 || j == 0) {
                    d[i][j]=0;
                    continue;
                } else if (s1.charAt(j-1) == s2.charAt(i-1)) {
                    d[i][j] = Math.max(Math.max(d[i][j - 1], d[i - 1][j]), d[i - 1][j - 1] + 1);
                } else {
                    d[i][j] = Math.max(d[i][j - 1], d[i - 1][j]);
                }
            }
        }
        System.out.println(d[s2.length()][s1.length()]);
    }

}
