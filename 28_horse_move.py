def func(n, m):
    base_num = 0
    dp = [[base_num] * (m + 2) for _ in range(n + 2)]

    for row in range(2, len(dp)):
        for col in range(2, len(dp[0])):
            if row == 2 and col == 2:
                dp[row][col] = 1
            else:
                dp[row][col] = dp[row-2][col-1] + dp[row-1][col-2]

    return dp[-1][-1]


if __name__ == "__main__":
    n, m = list(map(int, input().split()))

    res = func(n, m)
    print(res)
