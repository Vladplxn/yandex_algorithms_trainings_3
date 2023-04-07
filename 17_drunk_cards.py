from collections import deque

def func(deck_1, deck_2):
    deck_1 = deque(deck_1)
    deck_2 = deque(deck_2)

    cnt = 0
    while deck_1 and deck_2:
        card_1 = deck_1.popleft()
        card_2 = deck_2.popleft()

        if (card_1 > card_2 and (card_2 != 0 or card_1 != 9)) or (card_1 == 0 and card_2 == 9):
            deck_1.append(card_1)
            deck_1.append(card_2)
        else:
            deck_2.append(card_1)
            deck_2.append(card_2)
        
        cnt += 1
        if cnt == 10**6:
            return 'botva'
    
    if len(deck_1):
        return f'first {cnt}'
    else:
        return f'second {cnt}'


if __name__ == "__main__":
    deck_1 = list(map(int, input().split()))
    deck_2 = list(map(int, input().split()))

    print(func(deck_1, deck_2))