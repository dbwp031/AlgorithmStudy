package baek9663;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int[] col;
    static int n;
    static int answer = 0;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws Exception{
        n = Integer.parseInt(br.readLine());
        col = new int[n + 1];
        Arrays.fill(col,0);
        n_queens(1);
        System.out.println(answer);
    }

    private static void n_queens(int c) {
        if (c == n + 1) {
            answer++;
            return;
        }
        for (int i = 1; i < n + 1; i++) {
            col[c] = i;
            if (promising(c)) {
                n_queens(c+1);
            }
        }
    }

    private static boolean promising(int c) {
        boolean flag = true;
        for (int i = 1; i < c; i++) {
            if (col[i] == col[c] || Math.abs(col[i] - col[c]) == (c - i)) {
                flag = false;
                break;
            }
        }
        return flag;
    }
}

