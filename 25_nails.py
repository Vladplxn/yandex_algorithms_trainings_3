def func(coords):
    coords.sort()
    dp = [0] * len(coords)
    dp[0] = dp[1] = coords[1] - coords[0]
    for i in range(2, len(coords)):
        dp[i] = min(dp[i-1], dp[i-2]) + coords[i] - coords[i-1]
    
    return dp[-1]



if __name__ == "__main__":
    _ = int(input())
    coords = list(map(int, input().split()))
    

    print(func(coords))
