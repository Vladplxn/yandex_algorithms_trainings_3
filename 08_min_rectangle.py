def func(coords):
    min_xy, max_xy = list(coords[0]), list(coords[0])

    for x, y in coords:
        if x < min_xy[0]:
            min_xy[0] = x
        elif x > max_xy[0]:
            max_xy[0] = x
        
        if y < min_xy[1]:
            min_xy[1] = y
        elif y > max_xy[1]:
            max_xy[1] = y
    
    return min_xy + max_xy



if __name__ == "__main__":
    with open("08_min_rectangle_input.txt", 'r') as f:
        n, *coords = map(lambda x: tuple(int(el) for el in x.strip().split()), f.readlines())
    
    print(*func(coords))
