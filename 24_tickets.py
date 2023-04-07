def func(n, A, B, C):
    dp = [0] * (n + 3)
    A = ([3601] * 3) + A
    B = ([3601] * 3) + B
    C = ([3601] * 3) + C

    for i in range(3, n + 3):
        dp[i] = min(
            dp[i-1] + A[i],
            dp[i-2] + B[i-1],
            dp[i-3] + C[i-2]
        )
    
    return dp[-1]



if __name__ == "__main__":
    n = int(input())
    A, B, C = [], [], []
    for _ in range(n):
        a, b, c = list(map(int, input().split()))
        A.append(a)
        B.append(b)
        C.append(c)

    print(func(n, A, B, C))
