def func(way1):
    deadend = []
    way2 = []
    last_in_way2 = 0
    for wagon in way1:
        deadend.append(wagon)

        while len(deadend) and deadend[-1] == last_in_way2 + 1:
            way2.append(deadend.pop())
            last_in_way2 += 1
    
    return 'YES' if len(way1)==len(way2) else 'NO'



if __name__ == "__main__":
    _ = input()
    wagons = list(map(int, input().split()))

    print(func(wagons))