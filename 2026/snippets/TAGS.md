# 🏷️ Snippet Tags Standard

## 1) Core Tags (use these consistently)

### Algorithm / Technique
- `bfs`, `dfs`, `dijkstra`, `mst`, `union-find`, `toposort`
- `dp`, `greedy`, `binary-search`, `two-pointers`, `prefix-sum`

### Data Structure
- `queue`, `deque`, `heap`, `stack`, `hashmap`, `set`
- `segment-tree`, `fenwick`, `trie`

### Problem Shape
- `grid`, `graph`, `tree`, `string`, `math`
- `component`, `shortest-path`, `connectivity`, `reachability`

### State / Correctness
- `visited`, `wildcard`, `state`, `invariant`, `rollback`
- `tie-break`, `ordering`, `stable`

### Simulation
- `simulation`, `turn-loop`, `gravity`, `rotate`, `collision`, `movement`
- `obstacle`, `wall`

---

## 2) Importance & Difficulty Standard

### Importance
- `S`: Platinum/core interview skill, high reuse, easy to fail without it
- `A`: frequent in coding tests, strongly reusable
- `B`: sometimes useful, easy to derive on the fly
- `C`: niche or problem-specific

### Difficulty
- `Easy`: can implement reliably in 5~10 minutes
- `Medium`: common pitfalls, needs practice
- `Hard`: error-prone under pressure, requires mastery

---

## 3) File Naming Rules
- Use snake_case
- Prefer technique-first naming:
  - `global_vs_temp_visited.md`
  - `gravity_write_pointer.md`
  - `multi_key_max.md`

---

## 4) Category Mapping Rules
- `bfs/`: traversal + visited logic (including DFS)
- `simulation/`: grid transforms + turn logic
- `priority/`: ordering, tie-breaking, selection logic, heaps
- If unsure:
  - Put it where you will search first.