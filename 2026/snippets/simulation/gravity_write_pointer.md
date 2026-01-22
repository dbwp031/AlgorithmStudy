## Gravity with Write Pointer (Walls)

### When to use
- Grid simulation where blocks fall downward until a wall or bottom.
- Walls are fixed; empty cells are filled by falling blocks.

### Copy-paste code
```python
def apply_gravity(board, empty=-2, wall=-1):
    n = len(board)
    for c in range(n):
        write = n - 1
        for r in range(n - 1, -1, -1):
            if board[r][c] == wall:
                write = r - 1
            elif board[r][c] != empty:
                val = board[r][c]
                if write != r:
                    board[r][c] = empty
                    board[write][c] = val
                write -= 1
```

### Complexity
- Time: O(N^2)
- Space: O(1) extra

### Common mistakes
- Letting blocks pass through walls.
- Forgetting to move `write` after placing a block.
