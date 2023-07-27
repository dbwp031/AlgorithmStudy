package baek2295;

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    static int n;
    static List<Long> data, two;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        data = new ArrayList<>();
        two = new ArrayList<>();
        n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            data.add(Long.parseLong(br.readLine()));
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                two.add(data.get(i) + data.get(j));
            }
        }
        Collections.sort(two);

        long maxV = -1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                long k = data.get(j) - data.get(i);
                int find = Collections.binarySearch(two, k);
                if (find >= 0) {
                    maxV = Math.max(two.get(find)+data.get(i), maxV);
                }
            }
        }
        System.out.println(maxV);
    }

}
