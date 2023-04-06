def main():
    with open("input.txt", "r") as f:
        puzzle = f.read().splitlines()

    print("Part one:", part1(puzzle))
    print("Part two:", part2(puzzle))


def part1(p):
    elves = set()

    for r, line in enumerate(p):
        for c, item in enumerate(line):
            if item == "#":
                elves.add(c + r * 1j)

    scanmap = {
        -1j: [-1j - 1, -1j, -1j + 1],
        1j: [1j - 1, 1j, 1j + 1],
        1: [1 - 1j, 1, 1 + 1j],
        -1: [-1 - 1j, -1, -1 + 1j]
    }

    moves = [-1j, 1j, -1, 1]
    N = [-1 - 1j, -1j, -1j + 1, 1, 1 + 1j, 1j, 1j - 1, -1]

    for _ in range(10):
        once = set()
        twice = set()

        for elf in elves:
            if all(elf + x not in elves for x in N):
                continue
            for move in moves:
                if all(elf + x not in elves for x in scanmap[move]):
                    prop = elf + move
                    if prop in twice:
                        pass
                    elif prop in once:
                        twice.add(prop)
                    else:
                        once.add(prop)
                    break

        ec = set(elves)

        for elf in ec:
            if all(elf + x not in ec for x in N):
                continue
            for move in moves:
                if all(elf + x not in ec for x in scanmap[move]):
                    prop = elf + move
                    if prop not in twice:
                        elves.remove(elf)
                        elves.add(prop)
                    break

        moves.append(moves.pop(0))

    mx = min(x.real for x in elves)
    Mx = max(x.real for x in elves)
    my = min(x.imag for x in elves)
    My = max(x.imag for x in elves)

    return int((Mx - mx + 1) * (My - my + 1) - len(elves))


def part2(p):
    elves = set()

    for r, line in enumerate(p):
        for c, item in enumerate(line):
            if item == "#":
                elves.add(c + r * 1j)

    scanmap = {
        -1j: [-1j - 1, -1j, -1j + 1],
        1j: [1j - 1, 1j, 1j + 1],
        1: [1 - 1j, 1, 1 + 1j],
        -1: [-1 - 1j, -1, -1 + 1j]
    }

    moves = [-1j, 1j, -1, 1]
    N = [-1 - 1j, -1j, -1j + 1, 1, 1 + 1j, 1j, 1j - 1, -1]

    last = set(elves)

    iter = 1
    while True:
        once = set()
        twice = set()

        for elf in elves:
            if all(elf + x not in elves for x in N):
                continue
            for move in moves:
                if all(elf + x not in elves for x in scanmap[move]):
                    prop = elf + move
                    if prop in twice:
                        pass
                    elif prop in once:
                        twice.add(prop)
                    else:
                        once.add(prop)
                    break

        ec = set(elves)

        for elf in ec:
            if all(elf + x not in ec for x in N):
                continue
            for move in moves:
                if all(elf + x not in ec for x in scanmap[move]):
                    prop = elf + move
                    if prop not in twice:
                        elves.remove(elf)
                        elves.add(prop)
                    break

        moves.append(moves.pop(0))

        if last == elves:
            break

        last = set(elves)
        iter += 1

    mx = min(x.real for x in elves)
    Mx = max(x.real for x in elves)
    my = min(x.imag for x in elves)
    My = max(x.imag for x in elves)

    return iter


if __name__ == "__main__":
    main()
