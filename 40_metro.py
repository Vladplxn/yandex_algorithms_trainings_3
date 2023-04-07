from collections import deque


def build_graph(lines):
    graph = {idx: [] for idx in range(len(lines))}
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            if len(set(lines[i]).intersection(lines[j])) > 0:
                graph[i].append(j)
                graph[j].append(i)
    return graph


def func(graph, station_to_line, start, finish):
    found_results = []
    finish_lines = station_to_line[finish]
    queue = deque()
    visited = set()
    for idx in station_to_line[start]:
        queue.append((idx, 0))
        visited.add(idx)
    while queue:
        curr_idx, curr_len = queue.popleft()
        if curr_idx in finish_lines:
            found_results.append(curr_len)
        for neigh_idx in graph[curr_idx]:
            if neigh_idx not in visited:
                queue.append((neigh_idx, curr_len + 1))
                visited.add(neigh_idx)
    if len(found_results) > 0:
        return min(found_results)
    return -1


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    lines = []
    station_to_line = {idx: [] for idx in range(1, N + 1)}
    for idx_line in range(M):
        curr_line = []
        for el in list(map(int, input().split()))[1:]:
            curr_line.append(el)
            station_to_line[el].append(idx_line)
        lines.append(curr_line)
    start, finish = map(int, input().split())

    graph = build_graph(lines)
    print(func(graph, station_to_line, start, finish))
