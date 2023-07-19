# 최소 신장 트리 (Minimum Spanning Tree, MST)
방향성이 없는 그래프의 부분 그래프들 중에서 모든 정점을 포함하는 트리

참고) 트리의 성질: 정점이 V개일 때, 간선의 수는 V-1개

## 크루스칼 알고리즘
1. 간선을 크기의 오름차순으로 정렬하고 제일 낮은 비용의 간선을 선택
2. 현재 선택한 간선이 정점 u,v를 연결하는 간선이라고 할 때
  2.1. 만약 u와 v가 같은 그룹이라면) 아무 것도 하지 않고 넘어감
  2.2 다른 그룹이라면) 같은 그룹으로 만들고 현재 선택한 간선을 최소 신장 트리에 추가
3. 최소 신장 트리에 V-1개의 간선을 추가시켰다면 과정을 종료, 그렇지 않다면
그 다음으로 비용이 작은 간선을 선택한 후 2번 과정을 반복
```java
package baek1197;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.StringTokenizer;

class Node implements Comparable<Node> {
    int from, to, cost;

    public Node(int from, int to, int cost) {
        this.from = from;
        this.to = to;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node o) {
        return Integer.compare(this.cost, o.cost);
    }
}
public class Main {
    static int v,e;
    static int[] parents;
    static ArrayList<Node> nodeList;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());

        parents = new int[v + 1];
        nodeList = new ArrayList<>();

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            nodeList.add(new Node(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }
        Collections.sort(nodeList);
        
        make();
        
        int sum = 0;
        int cnt = 0;
        for (Node n : nodeList) {
            if (union(n.from, n.to)) {
                sum+=n.cost;
                cnt++;
                if(cnt==e-1) break;
            }
        }
        System.out.println(sum);
        
    }

    private static boolean union(int from, int to) {
        from = find(from);
        to = find(to);
        if(from == to) return false;
        else parents[to] = from;
        return true;
    }

    private static int find(int v) {
        if(parents[v]==v) return v;
        else return parents[v] = find(parents[v]);
    }
    private static void make() {
        for (int i = 1; i < v + 1; i++) {
            parents[i]=i;
        }
    }
}

```
## 프림 알고리즘
```java
```
