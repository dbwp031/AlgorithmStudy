package baek15649;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    static int n,m;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws Exception{
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        boolean[] state =  new boolean[n+1];
        Arrays.fill(state,false);
        backTrack(state,  new Stack<>());
    }
    private static void backTrack(boolean[] state, Stack<Integer> stack) {
        if (stack.size() == m) {
            stack.forEach(s -> System.out.print(s+" "));
            System.out.println();
//            System.out.println();
            return;
        }


        for (int i = 1; i < n + 1; i++) {
            if(state[i]) continue;
            stack.push(i);
            state[i] = true;
            backTrack(state, stack);
            state[i]=false;
            stack.pop();
        }
    }
}
