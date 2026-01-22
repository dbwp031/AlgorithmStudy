## Component BFS (Grid)

### When to use
- Find all connected components of same type in a grid.
- Need to gather cells, size, or metadata per component.

### Copy-paste code
```python
from collections import deque

def bfs_component(board, sr, sc, visited):
    n = len(board)
    target = board[sr][sc]
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    comp = [(sr, sc)]
    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if visited[nr][nc] or board[nr][nc] != target:
                continue
            visited[nr][nc] = True
            q.append((nr, nc))
            comp.append((nr, nc))
    return comp
```

### Complexity
- Time: O(N^2) over full traversal.
- Space: O(N^2) for visited.

### Common mistakes
- Forgetting to mark visited on push (causes duplicates).
- Allowing different values to join the same component.
