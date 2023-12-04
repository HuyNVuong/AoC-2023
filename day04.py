import re

def to_cards_and_numbers(line: str) -> tuple:
    cards_numbers_str = line.split(': ')[1].split(' | ')
    
    cards = [int(c) for c in re.findall(r'[0-9]+', cards_numbers_str[0])]
    numbers = [int(n) for n in re.findall(r'[0-9]+', cards_numbers_str[1])]

    return cards, numbers

with open('./data/day04.txt', 'r') as file:
    lines = file.read().split('\n')
    cards_numbers_list = [to_cards_and_numbers(line) for line in lines]
    ps = 0
    cc = {}
    for i, (cards, numbers) in enumerate(cards_numbers_list):
        p = 0
        w = 0
        for n in numbers:
            if n in cards:
                p = 1 if p == 0 else p * 2
                w += 1
        ps += p
        if w > 0:
            for j in range(i + 1, i + w + 1):
                if j not in cc:
                    cc[j] = 1
                cc[j] += (1 * cc.get(i, 1))
    print(ps)
    print(sum(cc.values()) + len(cards_numbers_list) - len(cc))
    