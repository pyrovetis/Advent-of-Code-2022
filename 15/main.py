import re


def main():
    with open("input.txt", "r") as f:
        puzzle = f.read().splitlines()

        print("Part one:", part1(puzzle))
        print("Part two:", part2(puzzle))


def parse_input(i):
    sensors = []
    regex = r"-?\d+"

    for line in i:
        sx, sy, bx, by = map(int, re.findall(regex, line))
        sensors.append((sx, sy, bx, by))

    return sensors


def part1(p):
    sensors = parse_input(p)
    Y = 2000000
    interval = []
    q = []
    known = set()
    cannot = set()

    for sx, sy, bx, by in sensors:
        r = abs(sx - bx) + abs(sy - by)
        o = r - abs(sy - Y)

        if o < 0:
            continue

        lx = sx - o
        hx = sx + o
        interval.append((lx, hx))

        if by == Y:
            known.add(bx)

    interval.sort()

    for low, high in interval:
        if not q:
            q.append([low, high])
            continue

        qlow, qhigh = q[-1]

        if low > qhigh + 1:
            q.append([low, high])
            continue

        q[-1][1] = max(high, qhigh)

    for low, high in q:
        for x in range(low, high + 1):
            cannot.add(x)

    return len(cannot - known)


def part2(p):
    sensors = parse_input(p)
    B = 4000000
    answer = 0

    for Y in range(B + 1):
        interval = []
        q = []
        x = 0

        for sx, sy, bx, by in sensors:
            r = abs(sx - bx) + abs(sy - by)
            o = r - abs(sy - Y)

            if o < 0:
                continue

            lx = sx - o
            hx = sx + o
            interval.append((lx, hx))

        interval.sort()

        for low, high in interval:
            if not q:
                q.append([low, high])
                continue

            qlow, qhigh = q[-1]

            if low > qhigh + 1:
                q.append([low, high])
                continue

            q[-1][1] = max(high, qhigh)

        for low, high in q:
            if x < low:
                answer = x * B + Y
                break
            x = max(x, high + 1)

            if x > B:
                break

    return answer


if __name__ == "__main__":
    main()
