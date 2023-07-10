import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] ascend = new int[n + 1];
        int[] descend = new int[n + 1];
        Arrays.fill(ascend, 1);
        Arrays.fill(descend, 1);
        int[] value = new int[n + 1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n+1; i++) {
            value[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 2; i < n + 1; i++) {
            for (int j = 1; j < i; j++) {
                if (value[j] < value[i]) {
                    ascend[i] = Math.max(ascend[j] + 1, ascend[i]);
                }
            }
        }

        for (int i = n - 1; i > 0; i--) {
            for (int j = n; j > i; j--) {
                if (value[i] > value[j]) {
                    descend[i] = Math.max(descend[j] + 1, descend[i]);
                }
            }
        }
        int maxCount = 0;
        for (int i = 1; i < n + 1; i++) {
            maxCount = Math.max(ascend[i] + descend[i] - 1, maxCount);
        }

//        System.out.println(Arrays.toString(ascend));
//        System.out.println(Arrays.toString(descend));
        System.out.println(maxCount);
    }
}
