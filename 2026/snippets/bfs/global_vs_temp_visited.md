## Global vs Temp Visited (Reusable Wildcards)

### When to use
- Grid/group BFS where some cells (e.g., rainbow/wildcard) can belong to multiple groups.
- You must avoid re-visiting normal cells across groups, but allow wildcard cells to be re-used per BFS.

### Copy-paste code
```python
from collections import deque

def bfs_group(start_r, start_c, board, normal_visited, wildcard_value=0):
    n = len(board)
    color = board[start_r][start_c]
    q = deque([(start_r, start_c)])
    normal_visited[start_r][start_c] = True
    group = [(start_r, start_c)]
    wildcard_visited = [[False] * n for _ in range(n)]

    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if board[nr][nc] == color and not normal_visited[nr][nc]:
                normal_visited[nr][nc] = True
                q.append((nr, nc))
                group.append((nr, nc))
            elif board[nr][nc] == wildcard_value and not wildcard_visited[nr][nc]:
                wildcard_visited[nr][nc] = True
                q.append((nr, nc))
                group.append((nr, nc))
    return group
```

### Complexity
- Time: O(N^2 + W * G) worst-case, where wildcard cells W may be re-visited per group G.
- Space: O(N^2) for visited tracking.

### Common mistakes
- Marking wildcard cells in `normal_visited` so they cannot be reused across groups.
- Forgetting to reset `wildcard_visited` per BFS.
- Starting BFS from a wildcard cell (should start from a normal cell).
