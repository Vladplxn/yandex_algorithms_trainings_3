from collections import defaultdict


def dfs(node, graph, visited, comp):
    visited.add(node)
    comp.append(node)
    for neigh in graph[node]:
        if neigh not in visited:
            dfs(neigh, graph, visited, comp)


def func(graph):
    visited = set()
    comps = []
    for node in graph:
        if node not in visited:
            curr_comp = []
            dfs(node, graph, visited, curr_comp)
            if curr_comp:
                comps.append(curr_comp)
    return comps


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    for el in range(1, n + 1):
        graph[el].append(el)

    if n == 0:
        print(0)
    else:
        res = func(graph)
        print(len(res))
        for el in res:
            print(len(el))
            print(*el)
