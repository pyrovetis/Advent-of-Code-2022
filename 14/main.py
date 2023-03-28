import numpy as np


def main():
    with open("input.txt", "r") as f:
        puzzle = f.read().splitlines()

    print("part one:", part1(puzzle))
    print("part two:", part2(puzzle))


SAND = "o"
ROCK = "#"
AIR = "."


def generate_cave(p):
    cave = np.full((318, 1000), AIR)
    lowest_depth = 0
    for j in p:
        path = j.split(" -> ")
        for i in range(len(path) - 1):
            p1, p2 = path[i].split(","), path[i + 1].split(",")
            x1, y1 = int(p1[0]), int(p1[1])
            x2, y2 = int(p2[0]), int(p2[1])

            points = points_on_line(x1, y1, x2, y2)
            for (x, y) in points:
                cave[y, x] = ROCK
                lowest_depth = max(y, lowest_depth)

    return cave, lowest_depth


def points_on_line(x1, y1, x2, y2):
    xrange = range(x1, x2 + 1) if x2 >= x1 else range(x2, x1 + 1)
    yrange = range(y1, y2 + 1) if y2 >= y1 else range(y2, y1 + 1)
    return [(x, y) for x in xrange for y in yrange]


def part1(p):
    cave, lowest = generate_cave(p)
    sand_count = 0

    while True:
        sand_count += 1
        r, c = 0, 500

        while True:
            if r > lowest:
                return sand_count - 1
            elif cave[r + 1, c] == AIR:
                r += 1
            elif cave[r + 1, c - 1] == AIR:
                r += 1
                c -= 1
            elif cave[r + 1, c + 1] == AIR:
                r += 1
                c += 1
            else:
                cave[r, c] = SAND
                break


def part2(p):
    cave, lowest = generate_cave(p)
    sand_count = 0
    floor = lowest + 2

    while True:
        sand_count += 1
        r, c = 0, 500

        while True:
            if cave[1, 499] == cave[1, 500] == cave[1, 501] == SAND:
                return sand_count
            elif r + 1 >= floor:
                cave[r, c] = SAND
                break
            elif cave[r + 1, c] == AIR:
                r += 1
            elif cave[r + 1, c - 1] == AIR:
                r += 1
                c -= 1
            elif cave[r + 1, c + 1] == AIR:
                r += 1
                c += 1
            else:
                cave[r, c] = SAND
                break


if __name__ == "__main__":
    main()
