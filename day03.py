import re
from typing import NamedTuple

class Engine(NamedTuple):
    value: int
    mx: int
    nx: int
    y: int

    def neighbors(self) -> list[tuple]:
        ns = [(self.mx - 1, self.y), (self.nx, self.y)]
        for x in range(self.mx - 1, self.nx + 1):
            ns.append((x, self.y - 1))
            ns.append((x, self.y + 1))

        return ns
    

with open('./data/day03.txt', 'r') as file:
    lines = file.read().split('\n')
    ps = {}
    engines = []
    gears = []
    for y, line in enumerate(lines):
        for m in re.finditer(r'([0-9]+)', line):
            mx, nx = m.span()
            engines.append(Engine(int(m.group()), mx, nx, y))
        for x, p in enumerate(line):
            ps[(x, y)] = p
            if p == '*':
                gears.append((x, y))

    total_sum = 0
    for engine in engines:
        if any([len(re.findall(r'[^0-9\.]', ps.get((x, y), '.'))) > 0 for x, y in engine.neighbors()]):
            total_sum += engine.value

    print(total_sum)

    gear_sum = 0
    for gx, gy in gears:
        eparts = []
        for e in engines:
            if any([ne == (gx, gy) for ne in e.neighbors()]):
                eparts.append(e)
        if len(eparts) == 2:
            gear_sum += eparts[0].value * eparts[1].value

    print(gear_sum)