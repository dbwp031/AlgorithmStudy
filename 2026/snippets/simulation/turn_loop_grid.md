## Turn Loop for Grid Simulation

### When to use
- Problems that repeat a fixed sequence of transformations per turn (find group -> delete -> gravity -> rotate).
- You must stop when no valid group/action remains.

### Copy-paste code
```python
def run_simulation(board):
    score = 0
    while True:
        ok, gained = find_and_remove(board)
        if not ok:
            break
        score += gained
        apply_gravity(board)
        board = rotate_90_left(board)
        apply_gravity(board)
    return score
```

### Complexity
- Depends on inner operations; typically O(T * N^2).

### Common mistakes
- Mutating `board` inconsistently (mixing in-place and returned copies).
- Forgetting to stop when no valid action exists.
- Applying transforms in the wrong order.
