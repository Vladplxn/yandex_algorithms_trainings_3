def dfs(start, graph, visited, arr):
    stack = [start]

    while stack:
        node = stack[-1]
        visited[node] = 1
        unvisited_neigh = []
        for neigh in graph[node]:
            if neigh not in visited:
                unvisited_neigh.append(neigh)
            elif visited[neigh] == 1:
                return False

        if unvisited_neigh:
            stack.append(unvisited_neigh[0])
        else:
            visited[node] = 2
            arr.append(node)
            stack.pop()
            
    return True


def func(graph):
    visited = {}
    arr = []

    for node in list(graph.keys()):
        if node not in visited:
            if dfs(node, graph, visited, arr) == False:
                return [-1]
    return arr[::-1]


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        graph = {i: [] for i in range(1, n+1)}
        for _ in range(m):
            n1, n2 = map(int, f.readline().split())
            graph[n1].append(n2)

    res = func(graph)
    if len(res) != n:
        print(-1)
    else:
        print(*res)
