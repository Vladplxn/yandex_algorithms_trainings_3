def func(line):
    stack = []
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    for ch in line:
        if ch in '([{':
            stack.append(ch)
        elif len(stack) > 0:
            popped_ch = stack.pop()
            if brackets[ch] != popped_ch:
                return 'no'
        else:
            return 'no'
    return 'yes' if len(stack) == 0 else 'no'


if __name__ == "__main__":
    line = input()

    print(func(line))