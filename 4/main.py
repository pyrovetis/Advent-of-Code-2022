def main():
    with open("input.txt", "r") as f:
        puzzle = f.readlines()

    print("First part:", part1(puzzle))
    print("Second part:", part2(puzzle))


def part1(puzzle):
    duplicates = 0

    for p in puzzle:
        section = [x.split("-") for x in p.split(",")]
        first_pair = set(range(
            int(section[0][0]),
            int(section[0][1])+1))
        second_pair = set(range(
            int(section[1][0]),
            int(section[1][1])+1))

        flag = all(elem in first_pair for elem in second_pair) or all(
            elem in second_pair for elem in first_pair)
        if flag:
            duplicates += 1

    return duplicates


def part2(puzzle):
    duplicates = 0

    for p in puzzle:
        section = [x.split("-") for x in p.split(",")]
        first_pair = set(range(
            int(section[0][0]),
            int(section[0][1])+1))
        second_pair = set(range(
            int(section[1][0]),
            int(section[1][1])+1))

        flag = any(elem in first_pair for elem in second_pair) or any(
            elem in second_pair for elem in first_pair)
        if flag:
            duplicates += 1

    return duplicates


if __name__ == "__main__":
    main()
