# 이진 탐색 트리
java에서는 `TreeSet, TreeMap`을 제공한다. **문제는 중복을 허용하지 않는다는 점이다.** **이는 TreeMap을 사용해서 value에 개수를 추가해줌으로써 어느정도 해소가 가능하다.**

중복을 허용하는 자료구조인 `TreeMultiset`은 구글에서 만든 고성능 java 라이브러리 Guava에서 제공한다. 하지만 위에서 말한 TreeMap과 거의 동일한 기능을 하는 것으로 확인된다. TreeMap으로 사용하면 될 듯 하다.
<details>
  <summary>TreeMultiset - insert, erase, update, find</summary>
  Guava의 `TreeMultiset`은 요소의 삽입(insert), 삭제(erase), 업데이트(update), 그리고 검색(find)을 위해 다양한 메서드를 제공합니다. 아래는 각각의 작업에 해당하는 주요 함수들을 설명합니다:

1. Insert (삽입):
   - `add(E element)`: 요소를 `TreeMultiset`에 추가합니다. 중복을 허용하므로 요소가 이미 존재하는 경우 해당 요소의 개수가 증가합니다.

2. Erase (삭제):
   - `remove(E element)`: 지정한 요소를 `TreeMultiset`에서 제거합니다. 해당 요소가 중복되면 하나의 요소만 제거됩니다.
   - `remove(E element, int occurrences)`: 지정한 개수만큼의 요소를 `TreeMultiset`에서 제거합니다.

3. Update (업데이트):
   - `setCount(E element, int count)`: 지정한 요소의 개수를 특정 값으로 설정합니다. 해당 요소가 이미 존재하는 경우 기존 개수가 새로운 값으로 변경됩니다.

4. Find (검색):
   - `count(E element)`: 지정한 요소의 개수를 반환합니다.
   - `size()`: `TreeMultiset`의 전체 요소 개수를 반환합니다.
   - `contains(E element)`: 지정한 요소가 `TreeMultiset`에 존재하는지 여부를 확인합니다.
   - `elementSet()`: 중복을 제거한 요소들의 집합(Set)을 반환합니다. (중복된 요소는 제외됩니다.)

아래는 각 작업에 해당하는 함수들을 사용하는 예제 코드입니다:

```java
import com.google.common.collect.TreeMultiset;

public class TreeMultisetExample {
    public static void main(String[] args) {
        TreeMultiset<String> treeMultiset = TreeMultiset.create();

        // Insert (삽입)
        treeMultiset.add("Apple");
        treeMultiset.add("Banana");
        treeMultiset.add("Banana"); // 중복 삽입

        // Erase (삭제)
        treeMultiset.remove("Apple");
        treeMultiset.remove("Banana", 1); // 하나만 삭제

        // Update (업데이트)
        treeMultiset.setCount("Banana", 3); // 개수를 3으로 업데이트

        // Find (검색)
        int bananaCount = treeMultiset.count("Banana");
        boolean containsBanana = treeMultiset.contains("Banana");
        int totalElements = treeMultiset.size();
        System.out.println("Banana 개수: " + bananaCount);
        System.out.println("Banana 포함 여부: " + containsBanana);
        System.out.println("전체 요소 개수: " + totalElements);

        // 요소 집합 반환
        System.out.println("중복 제거된 요소 집합: " + treeMultiset.elementSet());
    }
}
```

위 예제에서 `TreeMultiset`을 사용하여 각 작업에 해당하는 함수들을 활용하고 있습니다. 이를 통해 요소의 삽입, 삭제, 업데이트, 그리고 검색을 수행할 수 있습니다.
</details>
