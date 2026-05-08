import streamlit as st
import time
from main import dfs, draw_maze, bfs, astar

st.set_page_config(page_title="Maze Solver", page_icon="🧭")

st.title("🧭 Maze Solver")
st.caption("🟢 Start  |  🔴 End  |  ⬛ Wall  |  ⬜ Open  |  🔵 Exploring  |  🟡 Solution")
st.divider()

maze1 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,1,0,1,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,0,0,1,0,1,0,0,0,1],
    [1,0,1,0,1,0,1,1,1,0,1,1,1,0,1],
    [1,0,1,0,1,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,1,0,1],
    [1,0,1,1,1,1,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0,1,0,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
maze2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
maze3 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,0,1,0,1],
    [1,0,1,0,1,0,0,0,0,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,1,0,1,0,1,0,1,0,0,0,1],
    [1,1,1,0,1,0,1,0,1,0,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,0,1,1,1,0,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

if "results" not in st.session_state:
    st.session_state.results = {}

st.subheader("Select a Maze")
col1, col2, col3 = st.columns(3)
if col1.button("🗺️ Maze 1", width="stretch"):
    st.session_state.maze = maze1
    st.session_state.initialstate = (1, 1)
    st.session_state.goalstate = (11, 11)
if col2.button("🗺️ Maze 2", width="stretch"):
    st.session_state.maze = maze2
    st.session_state.initialstate = (1, 1)
    st.session_state.goalstate = (11, 11)
if col3.button("🗺️ Maze 3", width="stretch"):
    st.session_state.maze = maze3
    st.session_state.initialstate = (1, 1)
    st.session_state.goalstate = (11, 11)

st.divider()

placeholder = st.empty()
if "maze" in st.session_state:
    placeholder.code(
        draw_maze(st.session_state.maze, start=st.session_state.initialstate, end=st.session_state.goalstate),
        language=None,
    )

st.subheader("Run an Algorithm")
btn1, btn2, btn3 = st.columns(3)

def run_algo(name, fn):
    if "maze" not in st.session_state:
        st.warning("Please select a maze first!")
        return
    maze = st.session_state.maze
    initialstate = st.session_state.initialstate
    goalstate = st.session_state.goalstate

    timetake, memory, result = fn(initialstate, goalstate, maze)
    timetake = float(timetake)
    memory = float(memory)

    explored = []
    for cell in result[1]:
        explored.append(cell)
        placeholder.code(
            draw_maze(maze, highlight_cells=explored, start=initialstate, end=goalstate),
            language=None,
        )
        time.sleep(0.15)
    placeholder.code(
        draw_maze(maze, solution_cells=result[0], start=initialstate, end=goalstate),
        language=None,
    )

    st.session_state.results[name] = {
        "Steps": len(result[0]),
        "Time (s)": round(timetake, 6),
        "Memory (KB)": round(memory, 4),
    }

    st.success(f"✅ Path found! {len(result[0])} steps")
    m1, m2, m3 = st.columns(3)
    m1.metric("Steps", len(result[0]))
    m2.metric("Time", f"{timetake:.6f} s")
    m3.metric("Memory", f"{memory:.4f} KB")

if btn1.button("▶ Run BFS", width="stretch", type="primary"):
    run_algo("BFS", bfs)
if btn2.button("▶ Run DFS", width="stretch", type="primary"):
    run_algo("DFS", dfs)
if btn3.button("▶ Run A★", width="stretch", type="primary"):
    run_algo("A★", astar)

if len(st.session_state.results) > 1:
    st.divider()
    st.subheader("📊 Algorithm Comparison")
    rows = [{"Algorithm": algo, **data} for algo, data in st.session_state.results.items()]
    st.dataframe(rows, hide_index=True)

if st.session_state.results:
    if st.button("🗑️ Clear Results"):
        st.session_state.results = {}
        st.rerun()