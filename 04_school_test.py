def func(pupils, variants, p_row, p_col):
    p_place = 2 * (p_row - 1) + p_col
    p_variant = variants if p_place % variants == 0 else p_place % variants

    if p_variant * 2 > pupils:
        return [-1]
    
    v_place_list = []
    if p_place + variants <= pupils:
        v_place_list.append(p_place + variants)
    if p_place - variants > 0:
        v_place_list.append(p_place - variants)
    if len(v_place_list) == 0:
        return [-1]
    v_coord_list = []
    for v_place in v_place_list:
        d, m = divmod(v_place, 2)
        if m == 0:
            v_row = d
            v_col = 2
        else:
            v_row = d + 1
            v_col = 1
        v_coord_list.append((v_row, v_col))
    
    if len(v_coord_list) == 2:
        if abs(p_row - v_coord_list[0][0]) <= abs(p_row - v_coord_list[1][0]):
            return v_coord_list[0]
        else:
            return v_coord_list[1]

    return v_coord_list[0]



if __name__ == "__main__":
    with open("04_school_test_input.txt", 'r') as f:
        pupils, variants, p_row, p_col = map(lambda x: int(x.strip()), f.readlines())
    
    print(*func(pupils, variants, p_row, p_col))
