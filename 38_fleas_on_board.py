from collections import deque

N, M, S, T, Q = map(int, input().split())
S -= 1
T -= 1

d = [-1] * (N * M)
d[S * M + T] = 0

queue = deque([(S, T)])

while queue:
    u, v = queue.popleft()
    for du, dv in [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
    ]:
        nu, nv = u + du, v + dv
        if 0 <= nu < N and 0 <= nv < M and d[nu * M + nv] == -1:
            d[nu * M + nv] = d[u * M + v] + 1
            queue.append((nu, nv))

ans = 0
for i in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if d[x * M + y] == -1:
        print(-1)
        exit(0)
    ans += d[x * M + y]

print(ans)
