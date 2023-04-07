from collections import deque


def func(adj_matrix, start, finish):
    visited = set([start])
    queue = deque([(start, 0)])
    while queue:
        curr_idx, curr_len = queue.popleft()
        for idx, flag in enumerate(adj_matrix[curr_idx]):
            if flag == 1 and idx not in visited:
                if idx == finish:
                    return curr_len + 1
                queue.append((idx, curr_len + 1))
                visited.add(idx)
    return -1


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
        print(res)
