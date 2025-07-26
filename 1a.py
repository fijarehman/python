def dfs(graph, start):
    visited = set() 
    traversal = []

    def dfs_recursive(node):
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            for neighbor in graph[node]:
                dfs_recursive(neighbor)

    dfs_recursive(start)
    return traversal

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
dfs_result = dfs(graph, start_node)
print(f"DFS traversal starting from {start_node}: {dfs_result}")
