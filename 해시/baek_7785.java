package baek7785;

import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int n;
    static Set<String> logs;
//    static Map<String, String> logs;
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        logs = new HashSet<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String status = st.nextToken();
            if (Objects.equals(status, "enter")) {
                logs.add(name);
            } else {
                logs.remove(name);
            }
        }
        List<String> list = new ArrayList<>(logs);
//        Collections.reverse(list);
        list.sort(Collections.reverseOrder());
        for (String l : list) {
            System.out.println(l);
        }

    }

}
