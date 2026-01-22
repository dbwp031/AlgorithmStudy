# 🧯 Unblock Notes

## 1) What I Have Now
- Current approach summary:
  - BFS groups, pick max by size/rainbow/row/col, remove, gravity, rotate, gravity.
- Where I am stuck or confused:
  - Getting WA despite seemingly correct group selection.

---

## 2) Diagnosis
- Likely bug or missing logic:
  - The "standard block" inside a group is defined as the normal block with the smallest row, then smallest col. Your code uses the largest row/col instead, so tie-breaking is wrong when groups tie on size and rainbow count.
- Why this approach fails:
  - Group ranking uses the standard block position; using max instead of min changes the standard block and can choose the wrong group even though BFS and scoring look right.
- Minimal failing example (if applicable):
  - Two equal groups of size 2 with no rainbows: one group has normal blocks at (0,0)-(1,0), the other at (0,2)-(1,2). Standard blocks are (0,0) and (0,2). Correct tie-break chooses the group with standard block (0,2); using max-in-group can flip this.

---

## 3) Help in Levels

### Level 1 — Hint
- Conceptual direction only (no code):
  - Re-check the definition of "standard block" inside a group vs. how groups are compared. They are not the same "max" step.

---

### Level 2 — Guided Fix
- What to change:
  - Compute the standard block as the min (row, col) among non-rainbow blocks in the group, then compare groups by larger standard (row, col).
- Why this change works:
  - It matches the official tie-break: standard block is defined by smallest coordinates, and group selection prefers the largest standard block across groups.
- Invariant that must hold after the fix:
  - For every group, standard block = min normal block; group ordering uses size, rainbow count, then standard block row/col (descending).

---

### Level 3 — Optimal Answer
```python
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
EMPTY = -2
WALL = -1

board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def find_best_group(board):
    visited = [[False] * N for _ in range(N)]
    best = None  # (size, rainbow, std_row, std_col, cells)

    for i in range(N):
        for j in range(N):
            if board[i][j] <= 0 or visited[i][j]:
                continue

            color = board[i][j]
            q = deque()
            q.append((i, j))
            visited[i][j] = True

            group = [(i, j)]
            rainbow = []
            rvisited = [[False] * N for _ in range(N)]
            rvisited[i][j] = True

            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if board[nx][ny] == 0 and not rvisited[nx][ny]:
                        rvisited[nx][ny] = True
                        q.append((nx, ny))
                        group.append((nx, ny))
                        rainbow.append((nx, ny))
                    elif board[nx][ny] == color and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        group.append((nx, ny))

            if len(group) < 2:
                continue

            normals = [(r, c) for r, c in group if board[r][c] > 0]
            std_row, std_col = min(normals)
            cand = (len(group), len(rainbow), std_row, std_col, group)

            if best is None or cand[:4] > best[:4]:
                best = cand

    return best

def gravity(board):
    for c in range(N):
        write = N - 1
        for r in range(N - 1, -1, -1):
            if board[r][c] == WALL:
                write = r - 1
            elif board[r][c] != EMPTY:
                val = board[r][c]
                if write != r:
                    board[r][c] = EMPTY
                    board[write][c] = val
                write -= 1
    return board

def rotate_left(board):
    return [list(row) for row in zip(*board)][::-1]

score = 0
while True:
    best = find_best_group(board)
    if best is None:
        break

    size, _, _, _, cells = best
    score += size * size
    for r, c in cells:
        board[r][c] = EMPTY

    board = gravity(board)
    board = rotate_left(board)
    board = gravity(board)

print(score)
```

## 4) Snippet Extracted

Snippet: BFS Group with Rainbow Reuse
	•	Tags:
	•	Importance: A
	•	Difficulty: Medium
```python
# BFS for group with local rainbow-visited, global normal-visited
q = deque([(sr, sc)])
visited[sr][sc] = True
rvisited = [[False] * N for _ in range(N)]
rvisited[sr][sc] = True
group = [(sr, sc)]
rainbow = []

while q:
    x, y = q.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if board[nx][ny] == 0 and not rvisited[nx][ny]:
            rvisited[nx][ny] = True
            q.append((nx, ny))
            group.append((nx, ny))
            rainbow.append((nx, ny))
        elif board[nx][ny] == color and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny))
            group.append((nx, ny))
```

## 5) Next Practice (One Item)
•	One concrete follow-up exercise to reinforce this skill:  
Baekjoon 21609: re-implement with a clean comparator and verify tie-breaks using hand-crafted cases.
