from collections import deque

def display(state):
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()

def get_neighbors(state):
    neighbors = []
    blank = state.index(0)
    row = blank // 3
    col = blank % 3
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
    
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank], new_state[new_blank] = new_state[new_blank], new_state[blank]
            neighbors.append(tuple(new_state))
    return neighbors

def solve(start, goal):
    queue = deque([start])
    visited = {start}
    parent = {}  
    
    while queue:
        current = queue.popleft()
        
        if current == goal
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path
            
        for next_state in get_neighbors(current):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = current
                queue.append(next_state)
    return None

start = (0, 1, 3, 
         4, 2, 6, 
         7, 5, 8)

goal = (1, 2, 3, 
        4, 5, 6, 
        7, 8, 0)

print("START STATE:")
display(start)

solution = solve(start, goal)

if solution:
    print("SOLUTION:")
    for state in solution:
        display(state)
    print("Total moves:", len(solution) - 1)
else:
    print("No solution found.")
