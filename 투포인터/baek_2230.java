package baek2230;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n,m;
    static int[] arr;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);
        int minValue=2_000_000_001;
        int p1=1;
        int p2=1;
        // arr[p2] - arr[p1] >=M이면 p1 증가
        // else p2 증가
        //
        while (p2<=n && p1<=p2) {
            if (arr[p2] - arr[p1] == m) {
                minValue = m;
                break;
            }
            if (arr[p2] - arr[p1] < m) {
                p2++;
            } else {
                minValue = Math.min(minValue, arr[p2] - arr[p1]);
                p1++;
            }
        }
        System.out.println(minValue);
    }
}
