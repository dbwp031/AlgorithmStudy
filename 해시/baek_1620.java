package baek1620;

import java.io.*;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static String[] i2s;
    static Map<String, Integer> s2i;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        i2s = new String[n + 1];
        s2i = new HashMap<>();
        for (int i = 1; i < n+1; i++) {
            i2s[i] = br.readLine();
            s2i.put(i2s[i], i);
        }
        for (int i = 1; i < m + 1; i++) {
            String q = br.readLine();
            if (q.chars().allMatch(Character::isDigit)) {
                System.out.println(i2s[Integer.parseInt(q)]);
            } else {
                System.out.println(s2i.get(q));
            }
        }

    }
}
