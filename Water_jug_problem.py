from collections import deque

def water_jug(capacity_a, capacity_b, target):
    queue = deque()
    queue.append((0, 0))  # Fixed: Passed as a tuple
    visited = set()
    visited.add((0, 0))
    parent = {}           # Fixed: Changed to a dictionary to track paths
    action = {}
    
    while queue:
        a, b = queue.popleft()
        
        if a == target or b == target:
            current = (a, b)
            solution = []
            while current != (0, 0):
                solution.append((action[current], current))
                current = parent[current]
            solution.reverse()
            return solution
            
        # Fixed: Indented the next_states logic inside the while loop
        next_states = []
        next_states.append(((capacity_a, b), "Fill Jug A"))
        next_states.append(((a, capacity_b), "Fill Jug B"))
        next_states.append(((0, b), "Empty Jug A"))
        next_states.append(((a, 0), "Empty Jug B"))
        
        # Pour A -> B
        amount = min(a, capacity_b - b)
        next_states.append(((a - amount, b + amount), "Pour A -> B")) # Fixed: .append()
        
        # Pour B -> A
        amount = min(b, capacity_a - a)
        next_states.append(((a + amount, b - amount), "Pour B -> A")) # Fixed: .append()
        
        for state, operation in next_states:
            if state not in visited:
                visited.add(state)
                parent[state] = (a, b)
                action[state] = operation
                queue.append(state)
                
    return None

jug_a = 7
jug_b = 5  # Fixed: Corrected typo from jub_b
target = 6

print("WATER JUG PROBLEM")
print("Jug A capacity:", jug_a)
print("Jug B capacity:", jug_b)
print("Target amount:", target)

solution = water_jug(jug_a, jug_b, target)

if solution:
    print("\nInitial State: (0, 0)")
    for operation, state in solution:
        print(f"{operation} -> Jug A = {state[0]}, Jug B = {state[1]}")
else:
    print("No solution possible.")
