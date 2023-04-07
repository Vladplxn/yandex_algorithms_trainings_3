def func(word):
    d = {}
    for i in range(len(word)):
        if word[i] not in d:
            d[word[i]] = 0
        d[word[i]] += (i + 1) * (len(word) - i)
    return d


if __name__ == "__main__":
    with open("boring_lecture_input.txt", "r") as f:
        word = list(f.read().strip())

    res = func(word)
    for l in sorted(res.keys()):
        print(f"{l}: {res[l]}")
