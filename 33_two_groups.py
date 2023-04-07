from collections import defaultdict


def dfs(node, graph, visited, colors, prev_color):
    res = True
    visited.add(node)
    if colors.get(node, 0) == 0:
        colors[node] = 3 - prev_color

    for neigh in graph[node]:
        if colors[node] == colors.get(neigh, 0):
            return False
        if neigh not in visited:
            res = dfs(neigh, graph, visited, colors, colors[node])
    return res


def func(graph):
    visited = set()
    colors = {}
    is_yes = True

    for node in graph:
        if node not in visited:
            is_yes = dfs(node, graph, visited, colors, 1)
        if not is_yes:
            return "NO"
    return "YES"


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    if m == 0:
        print("YES")
    else:
        print(func(graph))
