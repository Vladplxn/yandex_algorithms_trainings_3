def func(line):
    stack = []
    
    for ch in line:
        if ch.isdecimal():
            stack.append(int(ch))
        else:
            el2 = stack.pop()
            el1 = stack.pop()
            if ch == '+':
                stack.append(el1 + el2)
            elif ch == '-':
                stack.append(el1 - el2)
            else:
                stack.append(el1 * el2)
    
    return stack[0]



if __name__ == "__main__":
    line = input().split()

    print(func(line))