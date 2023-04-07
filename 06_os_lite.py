def func(borders):
    s = set()
    for pair in borders:
        to_remove = []
        for set_pair in s:
            if set_pair[0] <= pair[1] and pair[0] <= set_pair[1]:
                to_remove.append(set_pair)
        s = s.difference(to_remove)
        s.add(pair)
    
    return len(s)


if __name__ == "__main__":
    with open("06_os_lite_input.txt", 'r') as f:
        _, _, *borders = map(lambda x: x.strip(), f.readlines())
        borders = list(map(lambda x: tuple(int(y) for y in x.split()), borders))
    
    print(func(borders))
