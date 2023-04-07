from collections import defaultdict


def dfs(node, graph, visited):
    visited.add(node)
    for neigh in graph[node]:
        if neigh not in visited:
            dfs(neigh, graph, visited)


def func(f_node, graph):
    visited = set()
    dfs(f_node, graph, visited)
    return len(visited), sorted(visited)


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = defaultdict(list)
    first_node = 1
    for _ in range(m):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    if len(graph) == 0:
        print(1)
        print(1)
    else:
        res = func(first_node, graph)
        print(res[0])
        print(*res[1])
