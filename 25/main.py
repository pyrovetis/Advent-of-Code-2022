def main():
    with open("input.txt", "r") as f:
        puzzle = f.read().splitlines()

    print("Part one:", part1(puzzle))
    print("Part two:", part2(puzzle))


def part1(p):
    total = 0

    for line in p:
        co = 1
        for x in line[::-1]:
            total += ("=-012".find(x) - 2) * co
            co *= 5

    result = ""

    while total:
        rem = total % 5
        total //= 5

        if rem <= 2:
            result = str(rem) + result
        else:
            result = "   =-"[rem] + result
            total += 1

    return result


def part2(p):
    pass


if __name__ == "__main__":
    main()
