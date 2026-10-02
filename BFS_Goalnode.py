from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

goal = 'D'

queue = deque(['A'])
visited = set()

while queue:
    node = queue.popleft()
    if node not in visited:
        print(node, end= "")
        if node == goal:
            print("\nGoal Not Found!")
            break
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)