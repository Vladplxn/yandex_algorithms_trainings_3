def func(matr):
    max_num = 21 * 101
    dp = [[max_num] + ([0] * (len(matr[0]))) for _ in range(len(matr))]
    dp = [[max_num] * (len(matr[0]) + 1)] + dp

    for row in range(1, len(dp)):
        for col in range(1, len(dp[0])):
            if row == 1 and col == 1:
                dp[row][col] = matr[row - 1][col - 1]
            else:
                dp[row][col] = (
                    min(dp[row - 1][col], dp[row][col - 1]) + matr[row - 1][col - 1]
                )

    return dp[-1][-1]


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    matr = []
    for _ in range(n):
        matr.append(list(map(int, input().split())))

    print(func(matr))
