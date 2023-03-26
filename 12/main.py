import nographs as nog


def main():
    with open("input.txt", "r") as f:
        puzzle = f.read().splitlines()

    print("Part one:", part1(puzzle))
    print("Part two:", part2(puzzle))


def elevation(c):
    return ord({"S": "a", "E": "z"}.get(c, c))


def part1(p):
    a = nog.Array(p)
    limits = a.limits()
    moves = nog.Position.moves()

    def next_vertex(pos: nog.Position, _):
        for pos2 in pos.neighbors(moves, limits):
            if elevation(a[pos2]) <= elevation(a[pos]) + 1:
                yield pos2

    start = a.findall("S")[0]
    end = a.findall("E")[0]

    f = nog.TraversalBreadthFirst(next_vertex).start_from(start)
    f.go_to(end)

    return f.depth


def part2(p):
    a = nog.Array(p)
    limits = a.limits()
    moves = nog.Position.moves()

    def next_vertex(pos: nog.Position, _):
        for pos2 in pos.neighbors(moves, limits):
            if elevation(a[pos2]) <= elevation(a[pos]) + 1:
                yield pos2

    start = a.findall("a")
    end = a.findall("E")[0]

    f = nog.TraversalBreadthFirst(next_vertex).start_from(start_vertices=start)
    f.go_to(end)

    return f.depth


if __name__ == "__main__":
    main()
