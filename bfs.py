from main import tracking
class node:
    def __init__(self,state,parent,action):
        self.state = state
        self.parent = parent
        self.action = action

def actionsequence(graph,goalstate , explored):
    solution = [goalstate]
    currentparet = graph[goalstate].parent

    while currentparet is not None:
        solution.append(currentparet)
        currentparet = graph[currentparet].parent

    solution.reverse()
    return solution , explored

@tracking
def bfs():
    initialstate = (2, 1) 
    goalstate = (0, 5)    

    maze = [
        [1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
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
                
                graph[(i,j)] = node((i,j),None,action)

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


print(bfs())