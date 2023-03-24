def main():
    with open("input.txt", "r") as f:
        puzzle = f.read().splitlines()

        print("Part one:", part1(puzzle))
        print("Part two:", part2(puzzle))


def part1(p):
    x = 1
    cycle = 0

    cycle_threshold = 20
    signal_strength = 0

    for item in p:
        cycle += 1
        if item.startswith("addx"):
            cycle += 1
            addx_value = int(item.split()[1])

            if cycle >= cycle_threshold:
                signal_strength += x * cycle_threshold
                cycle_threshold += 40

            x += addx_value

    return signal_strength


def run_cycle(cycle, x, lit_pixels):
    cycle += 1

    if x+2 >= cycle >= x:
        lit_pixels.append(cycle - 1)

    if cycle == 40:
        for i in range(40):
            print("#", end="") if i in lit_pixels else print(".", end="")
        print()
        lit_pixels.clear()
        cycle = 0

    return cycle


def part2(p):
    x = 1
    cycle = 0

    lit_pixels = []

    for item in p:
        cycle = run_cycle(cycle, x, lit_pixels)

        if item.startswith("addx"):
            cycle = run_cycle(cycle, x, lit_pixels)

            addx_value = int(item.split()[1])
            x += addx_value

    return "👆"


if __name__ == "__main__":
    main()
