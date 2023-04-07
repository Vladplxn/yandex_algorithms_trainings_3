def func(n, k):
    if n == 1:
        return 1
    k = min(n - 1, k)
    dp = [0] * (n + 1)
    for i in range(2, k + 2):
        dp[i] = sum(dp[:i]) + 1
    
    for i in range(k + 2, n + 1):
        dp[i] = sum(dp[i-k:i])
    
    return dp[n]



if __name__ == "__main__":
    n, k = list(map(int, input().split()))

    print(func(n, k))
