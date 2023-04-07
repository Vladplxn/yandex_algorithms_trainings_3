def func(n):
    dp = [0] * (n + 1)
    prev = [0] * (n + 1)

    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1
        prev[i] = i - 1

        if i % 2 == 0 and dp[i // 2] < dp[i] - 1:
            dp[i] = dp[i // 2] + 1
            prev[i] = i // 2
        if i % 3 == 0 and dp[i // 3] < dp[i] - 1:
            dp[i] = dp[i // 3] + 1
            prev[i] = i // 3
    
    path = [n]
    while path[-1] != 1:
        curr_num = prev[path[-1]]
        path.append(curr_num)
    
    return dp[n], path[::-1]



if __name__ == "__main__":
    n = int(input())

    res = func(n)
    print(res[0])
    print(*res[1])
