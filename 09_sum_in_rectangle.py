def func(shapes, matr, borders):
    results = []

    prefix_sum = [[0] * (shapes[1] + 1) for _ in range(shapes[0] + 1)]
    for i in range(1, shapes[0] + 1):
        for j in range(1, shapes[1] + 1):
            prefix_sum[i][j] = (
                matr[i - 1][j - 1]
                + prefix_sum[i - 1][j]
                + prefix_sum[i][j - 1]
                - prefix_sum[i - 1][j - 1]
            )

    for x_min, y_min, x_max, y_max in borders:
        results.append(
            prefix_sum[x_max][y_max]
            - prefix_sum[x_max][y_min - 1]
            - prefix_sum[x_min - 1][y_max]
            + prefix_sum[x_min - 1][y_min - 1]
        )

    return results


if __name__ == "__main__":
    with open("09_sum_in_rectangle_input.txt", "r") as f:
        shapes, *others = map(
            lambda x: tuple(int(el) for el in x.strip().split()), f.readlines()
        )
        matr = others[: shapes[0]]
        borders = others[shapes[0] :]

    for row in func(shapes, matr, borders):
        print(row)
