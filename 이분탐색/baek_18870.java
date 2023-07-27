package baek18870;

import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    static int n;
    static int[] data, carr;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static List<Integer> unique;
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        data = new int[n];
        carr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
            carr[i] = data[i];
        }
        Arrays.sort(data);
//        System.out.println(Arrays.toString(data));
        StringBuilder sb = new StringBuilder();
        unique = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (i == 0 || data[i - 1] != data[i]) {
                unique.add(data[i]);
            }
        }
//        System.out.println(Arrays.toString(unique.toArray()));
        for (int c : carr) {
            sb.append(bisect_left(c) + " ");
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    private static int bisect_left(int t) { //첫번째 t 인덱스
        int st = 0;
        int en = unique.size();
        while (st < en) {
            int mid = (st+en)/2;
            if(unique.get(mid) >= t) en = mid;
            else st = mid + 1;
        }
        return st;
    }
    private static int bisect_right(int t) { //첫번째 t 인덱스
        int st = 0;
        int en = unique.size();
        while (st < en) {
            int mid = (st+en)/2;
            if(unique.get(mid) > t) en = mid;
            else st = mid + 1;
        }
        return st;
    }
}
