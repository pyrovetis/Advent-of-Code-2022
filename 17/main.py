def main():
    with open("input.txt", "r") as f:
        puzzle = f.read().strip()
    print("Part one:", part1(puzzle))
    print("Part two:", part2(puzzle))


def part1(p):
    rocks = [
        [0, 1, 2, 3],
        [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
        [0, 1, 2, 2 + 1j, 2 + 2j],
        [0, 1j, 2j, 3j],
        [0, 1, 1j, 1 + 1j]
    ]
    jets = [1 if x == ">" else -1 for x in p]
    solid = {x - 1j for x in range(7)}
    height = 0
    rock_count = 0
    rock_index = 0
    rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]}

    while rock_count < 2022:
        for jet in jets:
            moved = {x + jet for x in rock}
            if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
                rock = moved
            moved = {x - 1j for x in rock}
            if moved & solid:
                solid |= rock
                rock_count += 1
                height = max(x.imag for x in solid) + 1
                if rock_count >= 2022:
                    break
                rock_index = (rock_index + 1) % 5
                rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]}
            else:
                rock = moved

    return int(height)


def part2(p):
    rocks = [
        [0, 1, 2, 3],
        [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
        [0, 1, 2, 2 + 1j, 2 + 2j],
        [0, 1j, 2j, 3j],
        [0, 1, 1j, 1 + 1j]
    ]
    T = 1000000000000
    jets = [1 if x == ">" else -1 for x in p]
    solid = {x - 1j for x in range(7)}
    height = 0
    seen = {}
    rock_count = 0
    rock_index = 0
    rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]}

    def summarize():
        o = [-20] * 7

        for x in solid:
            r = int(x.real)
            i = int(x.imag)
            o[r] = max(o[r], i)

        top = max(o)
        return tuple(x - top for x in o)

    while rock_count < T:
        for ji, jet in enumerate(jets):
            moved = {x + jet for x in rock}
            if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
                rock = moved
            moved = {x - 1j for x in rock}
            if moved & solid:
                solid |= rock
                rock_count += 1
                o = height
                height = max(x.imag for x in solid) + 1
                if rock_count >= T:
                    break
                rock_index = (rock_index + 1) % 5
                rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]}
                key = (ji, rock_index, summarize())
                if key in seen:
                    last_rock_count, last_height = seen[key]
                    rem = T - rock_count
                    rep = rem // (rock_count - last_rock_count)
                    offset = rep * (height - last_height)
                    rock_count += rep * (rock_count - last_rock_count)
                    seen = {}
                seen[key] = (rock_count, height)
            else:
                rock = moved

    return int(height + offset)


if __name__ == "__main__":
    main()
