package baek1806;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n,s;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[] arr;
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());

        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int p2=0;
        int partSum = 0;
        int len = n+1;
        for (int p1 = 0; p1 < n; p1++) {
            if (p1 == 0) {
                partSum = arr[0];
            } else {
                partSum -= arr[p1 - 1];
            }
            while (partSum < s) {
                if(p2+1>=n) break;
                p2++;
                partSum += arr[p2];
            }
            if (partSum >= s) {
                len = Math.min(p2-p1 +1,len);
            }
        }
        if(len==n+1) System.out.println(0);
        else System.out.println(len);
        
    }
}
