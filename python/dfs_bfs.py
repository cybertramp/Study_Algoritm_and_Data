import timeit


def bfs(graph, start_node):
    visit = {}
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit[node] = True
            queue.extend(graph[node])

    return visit


def dfs(graph, start_node):
    visit = {}
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit[node] = True
            stack.extend(graph[node])

    return visit

if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D', 'G'],
        'D': ['C', 'E'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

    start = timeit.default_timer()
    print(bfs(graph, 'A'))
    stop = timeit.default_timer()
    print(stop - start)
	
    print(dfs(graph, 'A'))
    stop = timeit.default_timer()
    print(stop - start)