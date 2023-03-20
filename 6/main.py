def main():
    with open("input.txt", "r") as f:
        puzzle = f.read()

    print("Part one:", part1(puzzle))
    print("Part two:", part2(puzzle))


def part1(p):
    p = list(p)
    answer = 0
    for i in range(len(p)):
        segment_start = i
        segment_end = i + 4 if len(p) > (i + 4) else len(p)-1
        reading = p[segment_start:segment_end]
        duplicates = [i for i in reading if reading.count(i) > 1]
        if not duplicates:
            answer = i + 4
            break
    return answer


def part2(p):
    p = list(p)
    answer = 0
    for i in range(len(p)):
        segment_start = i
        segment_end = i + 14 if len(p) > (i + 14) else len(p)-1
        reading = p[segment_start:segment_end]
        duplicates = [i for i in reading if reading.count(i) > 1]
        if not duplicates:
            answer = i + 14
            break
    return answer


if __name__ == "__main__":
    main()
