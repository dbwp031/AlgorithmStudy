package baek1920;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n,m;
    static int[] data;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
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
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            int target = Integer.parseInt(st.nextToken());
            sb.append(upper_idx(target, n) - lower_idx(target, n));
            sb.append(" ");
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();

    }

    private static int lower_idx(int target, int len) {
        int st = 1;
        int en = len +1; // 기존 크기보다 1 커야됨
        while (st < en) { // 크거나 같을 때가 아니라 클때
            int mid = (st+en)/2; // 소수 버림
            if(data[mid] >= target) en = mid; // en = mid -1 이 아니라 en=mid임
            // 왜냐하면 target이 data[mid]보다 크거나 "같을 때"라는 조건이기 때문이다.
            // 9 10 10 10 target: 10이라고 할때 가장 왼쪽 10에 걸리면 en이 9가 아니라 첫번째 10으로 가야한다.
            else st = mid+1;
            // target이 data[mid]보다 "클 때" 니깐 +1
        }
        return st; // st -> 첫번째 idx (mid는 target이하의 값을 가진다.
        // mid가 아니라 st를 return 하는 이유
        // st >= en인 경우
        // 9st 10mid en
        // 9st,mid 10en
        // 9mid 10st,en
        // st -> 첫번째 idx 리턴
        // st > en인 경우
        // 9st 10 10mid 10 en
        // 9st 10 10mid,en 10
        // 9st 10mid 10en 10
        // 9st 10mid,en 10 10
        // 9st,mid 10en 10 10
    }

    private static int upper_idx(int target, int len) {
        int st = 1;
        int en = len + 1;
        while (st < en) {
            int mid = (st+en)/2;
            if(data[mid] > target) en = mid;
            else st = mid+1;
        }
        return st;
        // 9st 10 10mid 11 en
        // 9 10 10 11st,mid en
        // 9 10 10 11st,mid,en
        // st: 10의 바로 오른쪽 idx
    }
}
