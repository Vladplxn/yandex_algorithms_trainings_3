def func(a, b, c):
    secs_between = 0
    rel_a = a[0] * 3600 + a[1] * 60 + a[2]
    rel_b = b[0] * 3600 + b[1] * 60 + b[2]
    rel_c = c[0] * 3600 + c[1] * 60 + c[2]

    if rel_c < rel_a:
        secs_between = rel_c + (24 * 3600 - rel_a)
    else:
        secs_between = rel_c - rel_a
    
    add_time = secs_between / 2
    res_time = int(rel_b + add_time + 0.5)

    return f"{int(res_time / 3600) % 24:{'02'}}:{int(res_time / 60) % 60:{'02'}}:{int(res_time % 60):{'02'}}"


if __name__ == "__main__":
    with open("sntp_input.txt", 'r') as f:
        a, b, c = map(lambda x: [int(el) for el in x.strip().split(':')], f.readlines())
    
    print(func(a, b, c))
