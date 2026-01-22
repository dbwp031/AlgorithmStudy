## Rotate 90 Degrees (Grid)

### When to use
- Grid simulation requiring 90-degree rotation (left/right).

### Copy-paste code
```python
def rotate_90_left(a):
    # (i, j) -> (N-1-j, i)
    return [list(row) for row in zip(*a)][::-1]

def rotate_90_right(a):
    # (i, j) -> (j, N-1-i)
    return [list(row) for row in zip(*a[::-1])]
```

### Complexity
- Time: O(N^2)
- Space: O(N^2)

### Common mistakes
- Mixing left/right direction.
- Mutating the original grid unexpectedly.
