from collections import deque


def find_start(cave):
    for z in range(len(cave)):
        for y in range(len(cave[0])):
            for x in range(len(cave[0][0])):
                if cave[z][y][x] == "S":
                    return (z, y, x)


def can_step(z, y, x, N, cave):
    if (0 <= z < N) and (0 <= y < N) and (0 <= x < N) and (cave[z][y][x] == "."):
        return True
    return False


def func(cave, N):
    start = find_start(cave)
    queue = deque([(*start, 0)])
    visited = set([start])
    while queue:
        z, y, x, path_len = queue.popleft()
        if z == 0:
            return path_len
        for dz, dy, dx in [
            (0, 0, 1),
            (0, 0, -1),
            (0, 1, 0),
            (0, -1, 0),
            (1, 0, 0),
            (-1, 0, 0),
        ]:
            new_z, new_y, new_x = z + dz, y + dy, x + dx
            if (
                can_step(new_z, new_y, new_x, N, cave)
                and (new_z, new_y, new_x) not in visited
            ):
                queue.append((new_z, new_y, new_x, path_len + 1))
                visited.add((new_z, new_y, new_x))
    return -1


if __name__ == "__main__":
    N = int(input())
    cave = []
    for z in range(N):
        _ = input()
        cave.append([list(input()) for _ in range(N)])

    print(func(cave, N))
