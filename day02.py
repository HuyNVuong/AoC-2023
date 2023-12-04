import re

def to_draw(line: str) -> dict[str, int]:
    dc = {}
    for d in line.split(', '):
        count, color = d.split(' ')
        dc[color] = int(count)
    
    return dc

def line_to_game(line: str) -> list[dict]:
    draws = [
        to_draw(draw_str) for draw_str in
        re.sub(r'Game ([0-9]+): ', '', line).split('; ')
    ]

    return draws

with open('./data/day02.txt', 'r') as file:
    lines = file.read().split('\n')
    games = [line_to_game(line) for line in lines]
    valid_game_count = 0
    for i, draws in enumerate(games):
        if all([draw.get('red', 0) <= 12 and draw.get('green', 0) <= 13 and draw.get('blue', 0) <= 14 for draw in draws]):
            valid_game_count += (i + 1)
    print(valid_game_count)
    
    power = 0
    for draws in games:
        rc = max([draw.get('red', 0) for draw in draws])
        gc = max([draw.get('blue', 0) for draw in draws])
        bc = max([draw.get('green', 0) for draw in draws])
        power += (rc * gc * bc)
    print(power)