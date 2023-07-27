package baek1654;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    static int n,k;
    static long[] wire;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static long maxV = 0;

    public static void main(String[] args) throws Exception{
        StringTokenizer st = new StringTokenizer(br.readLine());
        k = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        wire = new long[n];

        for (int i = 0; i < k; i++) {
            wire[i] = Long.parseLong(br.readLine());
            maxV = Math.max(maxV, wire[i]);
        }
        System.out.println(binary());
    }

    private static long binary() {
        long st = 1;
        long en = maxV;
        long maxLength = 0;
        while (st <= en) {
            long mid = (st+en)/2;
//            System.out.println(st + ", " + mid + ", " + en);
            if(check(mid)<n) en = mid-1;
            else if (check(mid) >= n) {
                maxLength = Math.max(maxLength, mid);
                st = mid+1;
            }
        }
        return maxLength;
    }

    private static long check(long length) {
        long count = 0;
        for (long w : wire) {
            count += w / length;
        }
        return count;
    }
}
