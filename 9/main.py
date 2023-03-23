import numpy as np


def main():
    with open("input.txt", "r") as f:
        puzzle = f.read().splitlines()

    print("Part one:", part1(puzzle))
    print("Part two:", part2(puzzle))


def part1(p):
    head = (0, 0)
    tail = (0, 0)

    visited = set()
    visited.add(tail)

    for i in p:
        direction, steps = i.split()

        for _ in range(int(steps)):
            match direction:
                case "U":
                    head = (head[0], head[1] + 1)
                case "D":
                    head = (head[0], head[1] - 1)
                case "R":
                    head = (head[0] + 1, head[1])
                case "L":
                    head = (head[0] - 1, head[1])

            x_diff = head[0] - tail[0]
            y_diff = head[1] - tail[1]

            if abs(x_diff) > 1 or abs(y_diff) > 1:
                tail = (tail[0] + np.sign(x_diff), tail[1] + np.sign(y_diff))
                visited.add(tail)

    return len(visited)


def part2(p):
    knots_count = 10
    knots = [(0, 0) for _ in range(knots_count)]

    visited = set()
    visited.add(knots[-1])

    for i in p:
        direction, steps = i.split()

        for _ in range(int(steps)):
            match direction:
                case "U":
                    knots[0] = (knots[0][0], knots[0][1] + 1)
                case "D":
                    knots[0] = (knots[0][0], knots[0][1] - 1)
                case "R":
                    knots[0] = (knots[0][0] + 1, knots[0][1])
                case "L":
                    knots[0] = (knots[0][0] - 1, knots[0][1])

            for k in range(knots_count-1):
                x_diff = knots[k][0] - knots[k+1][0]
                y_diff = knots[k][1] - knots[k+1][1]

                if abs(x_diff) > 1 or abs(y_diff) > 1:
                    knots[k+1] = (knots[k+1][0] + np.sign(x_diff),
                                  knots[k+1][1] + np.sign(y_diff))

                visited.add(knots[-1])

    return len(visited)


if __name__ == "__main__":
    main()
