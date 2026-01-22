# Repository Guidelines

## Project Structure & Module Organization
- `problems/`: solved Baekjoon problems in Python. Files are named by problem ID (e.g., `problems/3190.py`). Some problems use subfolders when multiple variants exist (e.g., `problems/21609/21609_2.py`).
- `snippets/`: reusable algorithm snippets and reference notes. Index and contribution rules live in `snippets/README.md`, and tag standards in `snippets/TAGS.md`.
- `prompts/`: writing templates and task checklists for reviews/unblockers.

## Build, Test, and Development Commands
- Run a solution locally:
  - `python3 problems/3190.py`  
    Use standard input; redirect files if needed (e.g., `python3 problems/3190.py < input.txt`).
- There is no build step or project-wide test runner; run individual scripts directly.

## Coding Style & Naming Conventions
- Language: Python for solutions.
- Indentation: 4 spaces; avoid tabs.
- Filenames: problem ID in numeric form; use `_2`, `_3` suffixes for alternative attempts (e.g., `14890_2.py`).
- Snippet files: snake_case and technique-first naming (e.g., `snippets/simulation/gravity_write_pointer.md`).
- Prefer clear variable naming for grid/graph problems (`r`, `c`, `nr`, `nc`, `dr`, `dc` are acceptable for tight loops).

## Testing Guidelines
- No automated tests are defined in this repository.
- Validate solutions by running against known sample inputs from Baekjoon.
- If adding a tricky solution, include a short comment with the key invariant or edge case it handles.

## Commit & Pull Request Guidelines
- Commit messages follow the BaekjoonHub format, for example:  
  `[Gold IV] Title: 뱀, Time: 100 ms, Memory: 110844 KB -BaekjoonHub`
- Keep commits scoped to one problem or snippet update.
- For PRs: include a brief description, the problem link or snippet purpose, and any notable edge cases tested.

## Snippet Contribution Rules
- Every snippet should include: when to use, copy-paste code, complexity, and common mistakes.
- Update `snippets/README.md` index table when adding a snippet, and follow tag standards in `snippets/TAGS.md`.
