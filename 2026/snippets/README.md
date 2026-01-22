# 🧩 Snippet Library

> Goal: Build reusable, interview-grade coding snippets for Baekjoon Gold → Platinum 3 and IT company coding tests.

## 0) How to Use This Library
- When solving a problem:
  - If you discover a reusable pattern, create/update a snippet file under `/snippets/<category>/`.
  - Add the snippet to the Index Table below.
- When stuck:
  - Search by Tags first.
  - Copy-paste the snippet, then adapt the condition logic.

---

## 1) Categories
- `bfs/` : BFS/DFS patterns, visited strategies, connected components, multi-source BFS
- `simulation/` : grid simulation (gravity/rotation), step-by-step state transitions
- `priority/` : multi-condition selection, heap patterns, tie-breaking
- `dp/` : classic DP templates
- `graph/` : Dijkstra, MST, topo sort, union-find
- `strings/` : KMP, rolling hash, trie
- `math/` : number theory, combinatorics

---

## 2) Tag Standard (Quick Reference)
See: `snippets/TAGS.md`

---

## 3) Index Table
| Snippet | Category | Tags | Importance | Difficulty | Link |
|---|---|---|---|---|---|
| Turn Loop for Grid Simulation | simulation | simulation, turn-loop, grid, state | A | Medium | `simulation/turn_loop_grid.md` |
| Global vs Temp Visited | bfs | bfs, visited, wildcard, grid | S | Hard | `bfs/global_vs_temp_visited.md` |
| Component BFS | bfs | bfs, grid, component | S | Medium | `bfs/component_bfs.md` |
| Gravity (Write Pointer) | simulation | simulation, grid, gravity, obstacle | A | Medium | `simulation/gravity_write_pointer.md` |
| Rotate 90° | simulation | simulation, grid, rotate | B | Easy | `simulation/rotate_90.md` |
| Multi-key Max Selection | priority | priority, tie-break, selection | A | Easy | `priority/multi_key_max.md` |
| Snake Simulation (Deque + Set) | simulation | simulation, grid, deque, set, collision, turn-loop | A | Medium | `simulation/snake_with_deque_and_set.md` |
| Robot Cleaner Turn Rule | simulation | simulation, grid, movement, state, turn-loop | A | Medium | `simulation/robot_cleaner_turn_rule.md` |
| Line Slope Check | simulation | simulation, grid, state, invariant | B | Medium | `simulation/line_slope_check.md` |

> Tip: Keep the table short and searchable. Each row must point to a real file.

---

## 4) Gold → Platinum 3 Learning Order (Recommended)
1. BFS component + boundary handling
2. Global vs temp visited (wildcards / re-usable nodes)
3. Priority selection with tie-breaking
4. Grid simulation: gravity / rotation / turn loop
5. Graph basics: union-find / Dijkstra / MST
6. State-heavy simulation and invariants

---

## 5) S-tier (Interview Critical)
- `bfs/global_vs_temp_visited.md`
- `bfs/component_bfs.md`
- (add more as you go)

---

## 6) Contribution Rules (for yourself)
- Each snippet must include:
  - When to use (problem patterns)
  - Copy-paste code
  - Complexity
  - Common mistakes
- Prefer minimal, correct, reusable code over full solutions.
