from collections import defaultdict

def criticalConnections(n, connections):
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    disc = [float('inf')] * n
    low = [float('inf')] * n
    parent = [-1] * n
    time = 0
    bridges = []

    def dfs(node):
        nonlocal time
        disc[node] = low[node] = time
        time += 1

        for neighbor in graph[node]:
            if disc[neighbor] == float('inf'):
                parent[neighbor] = node
                dfs(neighbor)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > disc[node]:
                    bridges.append([node, neighbor])
            elif neighbor != parent[node]:
                low[node] = min(low[node], disc[neighbor])

    for i in range(n):
        if disc[i] == float('inf'):
            dfs(i)

    return bridges