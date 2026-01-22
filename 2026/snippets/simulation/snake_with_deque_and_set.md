## Snake Simulation (Deque + Set)

### When to use
- Snake-like movement with growth and self-collision checks.
- Need O(1) collision detection.

### Copy-paste code
```python
from collections import deque

def simulate_snake(n, apples, turns):
    # apples: set of (r, c), turns: dict[time] = 'L'/'D'
    dr = (0, 1, 0, -1)
    dc = (1, 0, -1, 0)
    d = 0
    body = deque([(0, 0)])
    occupied = set([(0, 0)])
    t = 0
    while True:
        t += 1
        r, c = body[0]
        nr, nc = r + dr[d], c + dc[d]
        if not (0 <= nr < n and 0 <= nc < n) or (nr, nc) in occupied:
            return t
        body.appendleft((nr, nc))
        occupied.add((nr, nc))
        if (nr, nc) in apples:
            apples.remove((nr, nc))
        else:
            tr, tc = body.pop()
            occupied.remove((tr, tc))
        if t in turns:
            d = (d + 1) % 4 if turns[t] == "D" else (d - 1) % 4
```

### Complexity
- Time: O(T)
- Space: O(N^2) in worst case

### Common mistakes
- Checking collision before removing tail (only safe if you add head first and remove tail after).
- Using a list for body leading to O(N) search per step.
