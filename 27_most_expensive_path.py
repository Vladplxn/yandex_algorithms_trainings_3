def func(matr):
    min_num = -1
    dp = [[min_num] + ([0] * (len(matr[0]))) for _ in range(len(matr))]
    dp = [[min_num] * (len(matr[0]) + 1)] + dp

    for row in range(1, len(dp)):
        for col in range(1, len(dp[0])):
            if row == 1 and col == 1:
                dp[row][col] = matr[row - 1][col - 1]
            else:
                dp[row][col] = (
                    max(dp[row - 1][col], dp[row][col - 1]) + matr[row - 1][col - 1]
                )

    cur_row, cur_col = len(dp) - 1, len(dp[0]) - 1
    path = []
    while cur_row != 1 or cur_col != 1:
        if dp[cur_row - 1][cur_col] > dp[cur_row][cur_col - 1]:
            path.append("D")
            cur_row -= 1
        else:
            path.append("R")
            cur_col -= 1

    return dp[-1][-1], path[::-1]


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    matr = []
    for _ in range(n):
        matr.append(list(map(int, input().split())))

    res = func(matr)
    print(res[0])
    print(*res[1])
