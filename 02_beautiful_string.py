from collections import Counter


def func(k, s):
    max_beauty = 0
    cnt = Counter()
    l, r = 0, 0
    while r < len(s):
        max_reps_ch, max_reps_cnt = cnt.most_common(1)[0] if r > 0 else ('', 0)
        if max_reps_cnt + k >= r - l + 1 or max_reps_ch == s[r]:
            cnt[s[r]] += 1
            max_beauty = max(max_beauty, r-l+1)
            r += 1
        else:
            cnt[s[l]] -= 1
            l += 1
    return max_beauty


if __name__ == "__main__":
    with open("02_beautiful_string_input.txt", 'r') as f:
        k, s = map(lambda x: x.strip(), f.readlines())
        k = int(k)
    
    print(func(k, s))
