def func(arr):
    res = [-1] * len(arr)
    stack = []

    for idx, el in enumerate(arr):
        while stack and stack[-1][1] > el:
            prev_idx, _ = stack.pop()
            res[prev_idx] = idx
        stack.append((idx, el))
    
    return res


if __name__ == "__main__":
    _ = input()
    arr = list(map(int, input().split()))

    print(*func(arr))