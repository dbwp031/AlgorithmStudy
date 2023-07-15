# Union-Find 알고리즘
서로소 집합을 합치는 알고리즘

## 1. 부모-자식 관계를 모두 알아야 할 때
* 1의 부모가 2, 2의 부모가 3일 때 이 정보를 모두 담는 방법이다. 모든 정보를 확인할 수 있지만, 필요 없을 때엔 overhead가 발생한다.
```java
package find;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int[] parent;
    static int v, e;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws Exception{
        StringTokenizer st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        parent = new int[v + 1];

        for (int i = 1; i < v+1; i++) {
            parent[i]=i;
        }

        for (int i = 1; i < e + 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            union_parent(a, b);

            System.out.println(Arrays.toString(parent));
        }
    }

    private static void union_parent(int a, int b) {
        a = find_parent(a);
        b = find_parent(b);
        if(a<b) parent[b] = a;
        else parent[a]=b;
    }

    private static int find_parent(int a) {
        if(parent[a]!=a) return find_parent(parent[a]);
        else return a;
    }
}

```

```bash
"C:\Program Files\Java\jdk-17\bin\java.exe" "-javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2023.1\lib\idea_rt.jar=5397:C:\Program Files\JetBrains\IntelliJ IDEA 2023.1\bin" -Dfile.encoding=UTF-8 -classpath C:\Users\User\workspaces\algorithmStudy2\out\production\algorithmStudy2 find.Main
6 4
1 4
[0, 1, 2, 3, 1, 5, 6]
2 3
[0, 1, 2, 2, 1, 5, 6]
2 4
[0, 1, 1, 2, 1, 5, 6]
5 6
[0, 1, 1, 2, 1, 5, 5]

종료 코드 0(으)로 완료된 프로세스
```
## 2. 최상위 부모만 알면 될 때
parent table을 최상위 부모만 저장하도록 find_parent에서 계속 table을 업데이트 한다.
```java
package find;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int[] parent;
    static int v, e;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws Exception{
        StringTokenizer st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        parent = new int[v + 1];

        for (int i = 1; i < v+1; i++) {
            parent[i]=i;
        }

        for (int i = 1; i < e + 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            union_parent(a, b);

            System.out.println(Arrays.toString(parent));
        }
    }

    private static void union_parent(int a, int b) {
        a = find_parent(a);
        b = find_parent(b);
        if(a<b) parent[b] = a;
        else parent[a]=b;
    }
    private static int find_parent(int a) {
        if (parent[a] != a) {
            parent[a] = find_parent(parent[a]);
        }
        return parent[a];
    }
}
```
## find_parent 비교
### 버전 1. 모든 부모를 알아야 할 때
```java
    private static int find_parent(int a) {
        if(parent[a]!=a) return find_parent(parent[a]);
        else return a;
    }
```
### 버전 2. 최상위 부모만 알면 될 때
```java
    private static int find_parent(int a) {
        if (parent[a] != a) {
            parent[a] = find_parent(parent[a]);
        }
        return parent[a];
    }
```
