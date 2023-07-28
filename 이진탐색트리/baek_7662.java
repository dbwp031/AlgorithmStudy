package baek7662;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Objects;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class Main {
    static int t,k;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        t = Integer.parseInt(br.readLine());
        while (t>0) {
            t--;
            TreeMap<Long, Integer> tree = new TreeMap<>();
            k = Integer.parseInt(br.readLine());
            for (int i = 0; i < k; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String op = st.nextToken();
                long num = Long.parseLong(st.nextToken());
                if (op.equals("I")) {
                    if (tree.containsKey(num)) tree.put(num, tree.get(num) + 1);
                    else tree.put(num, 1);
                } else {
                    if (tree.isEmpty()) continue;
                    long key;
                    if(num == -1) key = tree.firstKey();
                    else key = tree.lastKey();

                    int count = tree.get(key);
                    if(count==1) tree.remove(key);
                    else tree.put(key, count - 1);
                    }
                }
            if(tree.isEmpty()) System.out.println("EMPTY");
            else System.out.println(tree.lastKey()+" "+tree.firstKey());
            }
        }
    }

