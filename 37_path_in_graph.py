from collections import deque


def func(adj_matrix, start, finish):
    queue = deque([start])
    path_from = {start: None}
    while queue:
        curr = queue.popleft()
        if curr == finish:
            res_path = [curr]
            prev = path_from[curr]
            while prev is not None:
                res_path.append(prev)
                prev = path_from[prev]
            return list(map(lambda x: x + 1, res_path[::-1]))
        for neigh, el in enumerate(adj_matrix[curr]):
            if el == 1 and neigh not in path_from:
                queue.append(neigh)
                path_from[neigh] = curr

    return []


if __name__ == "__main__":
    n = int(input())
    adj_matrix = []
    for _ in range(n):
        adj_matrix.append(list(map(int, input().split())))
    start, finish = list(map(int, input().split()))
    if start == finish:
        print(0)
    else:
        res = func(adj_matrix, start - 1, finish - 1)
        if len(res) == 0:
            print(-1)
        else:
            print(len(res) - 1)
            print(*res)
