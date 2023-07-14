# 다익스트라
특정 vertex에 대한 모든 vertex까지의 최소 거리 구하는 알고리즘  
간선의 weight가 음수가 있으면 사용하면 안되는 알고리즘 (음수 간선 있으면, 벨만 포드 알고리즘 써야됨) 
## 핵심
* priorityqueue써서 해결
* baek_1753.java 보면서 복기

priority queue를 사용하여 dijkstra 구현 가능하면 거의 다 풀 수 있음
```java
    private static void dijkstra(int start) {
        PriorityQueue<Node> queue = new PriorityQueue<>();
        boolean[] visited = new boolean[n+1];
        Arrays.fill(visited, false);
        queue.add(new Node(start, 0));
        dist[start]=0;

        while (!queue.isEmpty()) {
            Node curNode = queue.poll();
            int cur = curNode.end;

            if(visited[cur]) continue;
            visited[cur]=true;

            for (Node node : list[cur]) { // cur: 현재 노드 인덱스 node: cur 위치에서 갈 수 있는 vertex를 node.end로 가직 ㅗ있는 Node
                if (dist[node.end] > dist[cur] + node.weight) {
                    dist[node.end] = dist[cur] + node.weight;
                    queue.add(new Node(node.end, dist[node.end]));
//                    System.out.println(Arrays.toString(dist));
                }
            }

        }
    }
```
