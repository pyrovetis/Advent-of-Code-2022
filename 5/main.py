def main():
    with open("input.txt", "r") as f:
        puzzle = f.readlines()

    result_part1 = part1(puzzle)
    print("Part one:", "".join([i.pop() for i in result_part1]))
    result_part2 = part2(puzzle)
    print("Part two:", "".join([i.pop() for i in result_part2]))
    # print(result_part2)


def part1(p):
    # ship from file
    original_ship = p[:10]
    # instructions from file and reverse them
    instructions = list(reversed(p[10:]))
    # index of supplies on stacks
    stacks = list(reversed([i for i in range(36) if i % 2][0::2]))
    # make ship stacks
    ship = [[] for i in range(9)]

    # parse input file into list
    for i in range(9):
        x = stacks.pop()
        for j in range(8):
            ship[i].append(original_ship[j][x])

    # fix order of supplies in stacks
    ship = [list(reversed(i)) for i in ship]
    # remove space from lists
    for i in range(len(ship)):
        ship[i] = ' '.join(ship[i]).split()

    for i in range(len(instructions)):
        i = instructions.pop()
        i = i.split()

        move = range(int(i[1]))
        take_from = int(i[3])-1
        to = int(i[5])-1

        for j in move:
            ship[to].append(ship[take_from].pop())

    return ship


def part2(p):
    # ship from file
    original_ship = p[:10]
    # instructions from file and reverse them
    instructions = list(reversed(p[10:]))
    # index of supplies on stacks
    stacks = list(reversed([i for i in range(36) if i % 2][0::2]))
    # make ship stacks
    ship = [[] for i in range(9)]

    # parse input file into list
    for i in range(9):
        x = stacks.pop()
        for j in range(8):
            ship[i].append(original_ship[j][x])

    # fix order of supplies in stacks
    ship = [list(reversed(i)) for i in ship]
    # remove space from lists
    for i in range(len(ship)):
        ship[i] = ' '.join(ship[i]).split()

    for i in range(len(instructions)):
        i = instructions.pop()
        i = i.split()

        move = int(i[1])
        take_from = int(i[3])-1
        to = int(i[5])-1

        ship[to].extend(ship[take_from][-move:])
        ship[take_from] = ship[take_from][:-move]

    return ship


if __name__ == "__main__":
    main()
