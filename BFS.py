from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

queue = deque(['A'])
visited.set(['A'])

while queue:
    node = queue.popleft()
    print(node, end= " ")
    visited.add(node)
    
    for neighbour in graph[node]:
        if neighbour not in visited:
            queue.append(neighbour)
