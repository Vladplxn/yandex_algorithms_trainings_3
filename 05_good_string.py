def func(n, counts):
    res = 0
    for i in range(len(counts) - 1):
        res += min(counts[i], counts[i+1])
    
    return res
        


if __name__ == "__main__":
    with open("05_good_string_input.txt", 'r') as f:
        n, *counts = map(lambda x: int(x.strip()), f.readlines())
    
    print(func(n, counts))
