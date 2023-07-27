package baek1920;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n,m;
    static int[] data;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws Exception{
        n = Integer.parseInt(br.readLine());
        data = new int[n+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n+1; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(data, 1, n+1);
        m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            int result = Arrays.binarySearch(data, 1, n + 1, Integer.parseInt(st.nextToken()));
            System.out.println(result > 0 ? 1 : 0);

        }

    }

    private static int binarySearch(int target) {
        int st = 1;
        int en = n;
        while (st <= en) {
            int mid = (st + en) / 2;
            if (target > data[mid]) {
                st = mid+1;
            } else if (target < data[mid]) {
                en = mid - 1;
            } else {
                return 1;
            }
        }
        return 0;
    }
}
