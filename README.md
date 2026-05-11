# Algorithm Visualizer

A visual **Algorithm Visualization** web app built with **Streamlit** that demonstrates how search algorithms explore and solve problems in real time through animated grid-based environments.


## Features

- Interactive visualization of search algorithms on multiple environments
- Real-time exploration visualization showing how algorithms traverse the state space
- Three algorithm implementations — BFS, DFS, and A★
- Per-run metrics — steps taken, time elapsed, and memory used
- Side-by-side algorithm comparison table after running multiple solvers
- Performance tracked using a decorator with `time.perf_counter` and `tracemalloc`

## How the Program Works

Run the Streamlit web app and interact through the browser.

- Select a maze using the **Maze 1**, **Maze 2**, or **Maze 3** buttons
- The selected maze renders immediately in the terminal-style display
- Click **Run BFS**, **Run DFS**, or **Run A★** to start solving
- Watch the algorithm explore cells in real time (🔵), then highlight the final path (🟡)
- After running multiple algorithms, a comparison table appears automatically

### Legend

| Symbol | Meaning |
|---|---|
| 🟢 | Start position |
| 🔴 | Goal position |
| ⬛ | Wall |
| ⬜ | Open cell |
| 🔵 | Cell being explored |
| 🟡 | Final solution path |

### Algorithms

| Algorithm | Strategy | Guarantees Shortest Path |
|---|---|---|
| BFS | Explores level by level using a queue | ✅ Yes |
| DFS | Explores depth-first using a stack | ❌ No |
| A★ | Uses Manhattan distance heuristic + cost | ✅ Yes |

### Performance Metrics

| Metric | Description |
|---|---|
| Steps | Number of cells in the final solution path |
| Time (s) | Wall-clock time measured with `time.perf_counter` |
| Memory (KB) | Peak memory usage tracked with `tracemalloc` |

---

## How to Run Locally

### Prerequisites

- Python 3.9+

---

### Option 1: Install with pip

1. Clone the repository and navigate to the project folder:

```bash
git clone <your-repo-url>
cd maze-solver
```

2. (Optional but recommended) Create and activate a virtual environment:

```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install streamlit
```

4. Run the web app:

```bash
streamlit run webapp.py
```

---

### Option 2: Install with uv

1. Install **uv** (if not already installed):

```bash
pip install uv
```

2. Clone the repository and navigate to the project folder:

```bash
git clone <your-repo-url>
cd maze-solver
```

3. Sync the project environment:

```bash
uv sync
```

4. Run the web app:

```bash
uv run streamlit run webapp.py
```

---

Open the URL shown in the terminal (usually `http://localhost:8501`).

---

## Maze Layouts

All three mazes are 15×15 grids. The start is always `(1, 1)` and the goal is always `(11, 11)`.

| Maze | Description |
|---|---|
| Maze 1 | Winding corridors with multiple dead ends |
| Maze 2 | Segmented layout with isolated chambers |
| Maze 3 | Concentric spiral-like structure |

---

## File Structure

```
Maze-Solver/
│── main.py               # BFS, DFS, A★ implementations + draw_maze utility
│── webapp.py             # Streamlit web app (entry point)
│── pyproject.toml
│── uv.lock
│── .python-version
│── README.md
```

---

## How the Algorithms Are Implemented

### Graph Construction

Each maze is converted into a graph at runtime. Every open cell (`0`) becomes a node, and its passable neighbors become its actions (edges).

### Tracking Decorator

All three algorithm functions are wrapped with a `@tracking` decorator that measures execution time and peak memory:

```python
@tracking
def bfs(initialstate, goalstate, maze):
    ...
```

The decorator returns a tuple of `(time_taken, peak_memory_kb, result)`.

### Path Reconstruction

Once the goal is found, `actionsequence()` walks back through parent pointers to reconstruct the solution path from start to goal.

---

## Technologies Used

- Python
- [Streamlit](https://streamlit.io/) — Web UI framework
- [tracemalloc](https://docs.python.org/3/library/tracemalloc.html) — Memory profiling (standard library)
- [time](https://docs.python.org/3/library/time.html) — Performance timing (standard library)

---

## Notes

- The maze grid uses `0` for open cells and `1` for walls — the graph is built only from open cells.
- **DFS does not guarantee the shortest path** — it may find a longer route than BFS or A★.
- **A★ uses Manhattan distance** as the heuristic, which is admissible for grid mazes with 4-directional movement.
- The animation speed is fixed at `0.15s` per explored cell — this can be adjusted in `webapp.py`.
- Results persist in `st.session_state` for the duration of the session and can be cleared with the **Clear Results** button.
- Running the same algorithm again on a new maze will overwrite its previous result in the comparison table.

---

## Author

Muhammad Awais Tariq

---

If you like this project, consider giving it a star ⭐