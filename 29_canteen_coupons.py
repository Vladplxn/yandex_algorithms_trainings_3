def func(prices):
    max_num = 101 * 301
    if prices[0] > 100:
        dp = [prices[0], prices[0]] + [max_num] * (len(prices) - 2)
    else:
        dp = [prices[0]] + [max_num] * (len(prices) - 1)
    dp = [dp] + [[0] * len(prices) for _ in range(len(prices) - 1)]

    for day in range(1, len(dp)):
        for num_coupons in range(len(dp[0])):
            plus_coupon = max_num
            if num_coupons > 0 and prices[day] > 100:
                plus_coupon = prices[day] + dp[day - 1][num_coupons - 1]
            minus_coupon = max_num
            if num_coupons < (len(dp[0]) - 1):
                minus_coupon = dp[day - 1][num_coupons + 1]
            dp[day][num_coupons] = min(
                (dp[day - 1][num_coupons] + prices[day]), plus_coupon, minus_coupon
            )

    optimal_spend = min(dp[-1])
    coupons_left = dp[-1].index(optimal_spend)
    coupons_days = []

    prev_nc = coupons_left
    prev_spend = optimal_spend
    for day in range(len(prices) - 2, -1, -1):
        diff = (0, max_num, max_num)
        for idx, n_c in enumerate(range(len(dp[0]))):
            if prev_spend >= dp[day][n_c] and prev_spend - dp[day][n_c] <= diff[1]:
                diff = (idx, prev_spend - dp[day][n_c], dp[day][n_c])
        if diff[0] > prev_nc:
            coupons_days.append(day + 2)
        prev_nc = diff[0]
        prev_spend = diff[2]

    return optimal_spend, (coupons_left, len(coupons_days)), coupons_days[::-1]


if __name__ == "__main__":
    n = int(input())
    prices = []
    for _ in range(n):
        prices.append(int(input()))

    res = func(prices)
    print(res[0])
    print(*res[1])
    for el in res[2]:
        print(el)
