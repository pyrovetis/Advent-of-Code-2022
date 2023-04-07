import math
from collections import deque


def main():
    with open("input.txt", "r") as f:
        puzzle = f.read().splitlines()

    print("Part one:", part1(puzzle))
    print("Part two:", part2(puzzle))


def part1(p):
    blizzards = tuple(set() for _ in range(4))

    for r, line in enumerate(p[1:]):
        for c, item in enumerate(line[1:]):
            if item in "<>^v":
                blizzards["<>^v".find(item)].add((r, c))

    queue = deque([(0, -1, 0)])
    seen = set()
    target = (r, c - 1)

    lcm = r * c // math.gcd(r, c)

    while queue:
        time, cr, cc = queue.popleft()

        time += 1

        for dr, dc in ((0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)):
            nr = cr + dr
            nc = cc + dc

            if (nr, nc) == target:
                return time

            if (nr < 0 or nc < 0 or nr >= r or nc >= c) and not (nr, nc) == (-1, 0):
                continue

            fail = False

            if (nr, nc) != (-1, 0):
                for i, tr, tc in ((0, 0, -1), (1, 0, 1), (2, -1, 0), (3, 1, 0)):
                    if ((nr - tr * time) % r, (nc - tc * time) % c) in blizzards[i]:
                        fail = True
                        break

            if not fail:
                key = (nr, nc, time % lcm)

                if key in seen:
                    continue

                seen.add(key)
                queue.append((time, nr, nc))


def part2(p):
    blizzards = tuple(set() for _ in range(4))

    for r, line in enumerate(p[1:]):
        for c, item in enumerate(line[1:]):
            if item in "<>^v":
                blizzards["<>^v".find(item)].add((r, c))

    queue = deque([(0, -1, 0, 0)])
    seen = set()
    target = [(r, c - 1), (-1, 0)]

    lcm = r * c // math.gcd(r, c)

    while queue:
        time, cr, cc, stage = queue.popleft()

        time += 1

        for dr, dc in ((0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)):
            nr = cr + dr
            nc = cc + dc

            nstage = stage

            if (nr, nc) == target[stage % 2]:
                if stage == 2:
                    return time
                nstage += 1

            if (nr < 0 or nc < 0 or nr >= r or nc >= c) and (nr, nc) not in target:
                continue

            fail = False

            if (nr, nc) != target:
                for i, tr, tc in ((0, 0, -1), (1, 0, 1), (2, -1, 0), (3, 1, 0)):
                    if ((nr - tr * time) % r, (nc - tc * time) % c) in blizzards[i]:
                        fail = True
                        break

            if not fail:
                key = (nr, nc, nstage, time % lcm)

                if key in seen:
                    continue

                seen.add(key)
                queue.append((time, nr, nc, nstage))


if __name__ == "__main__":
    main()
