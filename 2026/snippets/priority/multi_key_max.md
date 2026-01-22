## Multi-key Max Selection (Tie-break)

### When to use
- You must select the best candidate by multiple ordered rules.
- Typical for "largest size, then largest X, then largest row/col".

### Copy-paste code
```python
def pick_best(groups):
    # groups: iterable of objects/dicts with comparable fields
    return max(
        groups,
        key=lambda g: (g.size, g.rainbow, g.row, g.col),
    )
```

### Complexity
- Time: O(K) to scan K candidates.
- Space: O(1) extra.

### Common mistakes
- Reversing a tie-break (min vs max).
- Including invalid candidates (size < 2).
- Comparing rows/cols in the wrong direction.
