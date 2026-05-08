import time
import tracemalloc

def tracking(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        tracemalloc.start()
        result = func(*args, **kwargs)
        current , peak  = tracemalloc.get_traced_memory()
        end = time.perf_counter()
        time_taken = end - start
        tracemalloc.stop()
        return f"{time_taken:.6f}" , f"{peak/(1024):.2f}" , result 
    return wrapper

class node:
    def __init__(self,state,action):
        self.state = state
        self.parent = None
        self.action = action
        self.costfromstart = float("inf")

def actionsequence(graph,goalstate , explored):
    solution = [goalstate]
    currentparet = graph[goalstate].parent

    while currentparet is not None:
        solution.append(currentparet)
        currentparet = graph[currentparet].parent

    solution.reverse()
    return solution , explored


@tracking
def bfs(initialstate , goalstate ,maze):
    rows, cols = len(maze), len(maze[0])   
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    graph = {}

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 0:
                action = []
                for move in moves:
                    nr ,nc = i+move[0] , j+move[1]
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                        action.append((nr,nc))
                
                graph[(i,j)] = node((i,j),action)

    frontier = [initialstate]
    explored = []

    while frontier:
        currentnode = frontier.pop(0)

        if graph[currentnode].state == goalstate:
            return actionsequence(graph,goalstate, list(explored))
        
        if currentnode not in explored:
            explored.append(currentnode)

        for child in graph[currentnode].action:

            if child not in explored and child not in frontier:
                graph[child].parent = graph[currentnode].state

                if graph[child].state == goalstate:
                    return actionsequence(graph,goalstate , list(explored))
                frontier.append(child)


@tracking
def dfs(initialstate , goalstate ,maze):
    rows, cols = len(maze), len(maze[0])   
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    graph = {}

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 0:
                action = []
                for move in moves:
                    nr ,nc = i+move[0] , j+move[1]
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                        action.append((nr,nc))
                
                graph[(i,j)] = node((i,j),action)

    frontier = [initialstate]
    explored = []

    while frontier:
        currentnode = frontier.pop()

        if graph[currentnode].state == goalstate:
            return actionsequence(graph,goalstate, list(explored))
        
        if currentnode not in explored:
            explored.append(currentnode)

        for child in graph[currentnode].action:

            if child not in explored and child not in frontier:
                graph[child].parent = graph[currentnode].state

                if graph[child].state == goalstate:
                    return actionsequence(graph,goalstate , list(explored))
                frontier.append(child)

def calculateheuristic(state,goalstate):
    x1 , y1 = state
    x2 , y2 = goalstate

    heuristic = abs(x2-x1) + abs(y2-y1)

    return heuristic

@tracking
def astar(intialstate , goalstate ,maze):
    graph = {}
    rows, cols = len(maze), len(maze[0])   
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 0:  
                action = []
                moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for move in moves:
                    nr,nc = i+move[0] , j+move[1]
                    if 0<=nr<rows and 0<=nc<cols and maze[nr][nc] == 0:
                        action.append(((nr,nc),1))
                    
                graph[(i,j)] = node((i,j),action)

    frontier = [(0,intialstate)]
    explored = set()

    graph[intialstate].costfromstart = 0
    while frontier:
        frontier.sort()
        heuristiccost , currentnode = frontier.pop(0)

        if currentnode == goalstate:
            return actionsequence(graph , goalstate , explored)
        
        explored.add(currentnode)

        for child,cost in graph[currentnode].action:
            newcost = graph[currentnode].costfromstart + cost
            newheuristic = newcost + calculateheuristic(child,goalstate)
            if child in explored:
                continue

            if newcost < graph[child].costfromstart:
                graph[child].parent = currentnode
                graph[child].costfromstart = newcost

                frontier.append((newheuristic,child))
    
    return None

def draw_maze(maze, highlight_cells=[], solution_cells=[], start=None, end=None):
    rows, cols = len(maze), len(maze[0])
    colors = []
    for r in range(rows):
        row_colors = []
        for c in range(cols):
            if (r, c) == start:
                row_colors.append("🟢")
            elif (r, c) == end:
                row_colors.append("🔴")
            elif (r, c) in solution_cells:
                row_colors.append("🟡")
            elif (r, c) in highlight_cells:
                row_colors.append("🔵")
            elif maze[r][c] == 1:
                row_colors.append("⬛")
            else:
                row_colors.append("⬜")
        colors.append(" ".join(row_colors))
    return "\n".join(colors)

if __name__ == "__main__":
    initialstate = (1,1) 
    goalstate = (11,11)    

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

    maze3 =  [
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

    option = int(input("Enter your option : "))

    if option == 1:
        print(bfs(initialstate ,goalstate ,  maze1 ))
        print(dfs(initialstate ,goalstate ,  maze1 ))
        print(astar(initialstate ,goalstate ,  maze1 ))        
    elif option == 2:
        print(bfs(initialstate ,goalstate ,  maze2 ))
        print(dfs(initialstate ,goalstate ,  maze2 ))
        print(astar(initialstate ,goalstate ,  maze2 ))
    else:
        print(bfs(initialstate ,goalstate ,  maze3 ))
        print(dfs(initialstate ,goalstate ,  maze3 ))
        print(astar(initialstate ,goalstate ,  maze3 ))        
