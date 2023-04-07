def func(n, stickers, k, collectors):
    sorted_stickers = sorted(set(stickers))
    sorted_collectors = sorted(list(zip(collectors, range(len(collectors)))), key=lambda x: x[0])
    res = []
    l = r = cntr = 0
    while l < len(sorted_stickers) and r < len(sorted_collectors):
        if sorted_stickers[l] < sorted_collectors[r][0]:
            cntr += 1
            l += 1
        else:
            res.append(cntr)
            r += 1
    if len(res) < len(sorted_collectors):
        res += [cntr] * (len(sorted_collectors) - len(res))
    
    res = sorted(zip(res, [x[1] for x in sorted_collectors]), key=lambda x: x[1])

    print(*[x[0] for x in res], sep='\n')



if __name__ == "__main__":
    with open("03_collector_diego_input.txt", 'r') as f:
        n, stickers, k, collectors = map(lambda x: x.strip(), f.readlines())
        n = int(n)
        stickers = set(map(int, stickers.split()))
        k = int(k)
        collectors = list(map(int, collectors.split()))
    
    func(n, stickers, k, collectors)
