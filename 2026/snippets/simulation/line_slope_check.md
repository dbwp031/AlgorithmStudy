## Line Slope Check (One-Dimensional)

### When to use
- Validate a line (row/col) where slopes of length L can be placed.
- Must ensure each cell is used by at most one slope.

### Copy-paste code
```python
def line_ok(line, L):
    n = len(line)
    used = [False] * n
    for i in range(n - 1):
        if line[i] == line[i + 1]:
            continue
        diff = line[i + 1] - line[i]
        if abs(diff) != 1:
            return False
        if diff == 1:  # up
            for j in range(i, i - L, -1):
                if j < 0 or line[j] != line[i] or used[j]:
                    return False
                used[j] = True
        else:  # down
            for j in range(i + 1, i + 1 + L):
                if j >= n or line[j] != line[i + 1] or used[j]:
                    return False
                used[j] = True
    return True
```

### Complexity
- Time: O(N * L) per line
- Space: O(N)

### Common mistakes
- Allowing overlap (not tracking `used`).
- Skipping boundary checks in slope placement loops.
