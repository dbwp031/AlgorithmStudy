## Robot Cleaner Turn Rule (Simulation)

### When to use
- Turn-based grid with "clean if dirty, else rotate, else move back" rules.
- Directional movement with deterministic rotation order.

### Copy-paste code
```python
def robot_clean(board, r, c, d):
    # 0:N, 1:E, 2:S, 3:W
    dr = (-1, 0, 1, 0)
    dc = (0, 1, 0, -1)
    NOT_CLEANED, WALL, CLEANED = 0, 1, 2
    cleaned = 0
    n, m = len(board), len(board[0])
    while True:
        if board[r][c] == NOT_CLEANED:
            board[r][c] = CLEANED
            cleaned += 1

        has_dirty = False
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == NOT_CLEANED:
                has_dirty = True
                break

        if not has_dirty:
            back = (d + 2) % 4
            nr, nc = r + dr[back], c + dc[back]
            if board[nr][nc] == WALL:
                return cleaned
            r, c = nr, nc
            continue

        for _ in range(4):
            d = (d - 1) % 4
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == NOT_CLEANED:
                r, c = nr, nc
                break
```

### Complexity
- Time: O(N*M) in worst case
- Space: O(1) extra

### Common mistakes
- Forgetting to stop when the back cell is a wall.
- Rotating in the wrong direction or order.
