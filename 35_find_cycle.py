def dfs(node_idx, visited, adj_matrix, prev_idx, path):
    visited[node_idx] = 1

    for neigh_idx, val in enumerate(adj_matrix[node_idx]):
        if val == 1:
            if neigh_idx != prev_idx and visited.get(neigh_idx, 0) == 1:
                return (False, neigh_idx)
            if neigh_idx not in visited:
                path.append(neigh_idx)
                res = dfs(neigh_idx, visited, adj_matrix, node_idx, path)
                if res[0] is False:
                    return res
                path.pop()
    visited[node_idx] = 2
    return (True,)


def func(adj_matrix):
    visited = {}

    for idx in range(len(adj_matrix)):
        path = [idx, ]
        res = dfs(idx, visited, adj_matrix, -1, path)
        if res[0] is False:
            cycle = path[path.index(res[1]) :]
            return (True, cycle)
    return (False,)


if __name__ == "__main__":
    n = int(input())
    adj_matrix = []
    for _ in range(n):
        adj_matrix.append(list(map(int, input().split())))

    res = func(adj_matrix)
    if res[0] is True:
        print("YES")
        print(len(res[1]))
        print(*list(map(lambda x: x+1, res[1])))
    else:
        print("NO")
