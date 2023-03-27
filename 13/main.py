from ast import literal_eval
from functools import cmp_to_key


def main():
    with open("input.txt", "r") as f:
        puzzle = f.read().splitlines()

    print("Part one:", part1(puzzle))
    print("Part two:", part2(puzzle))


def com(a, b):
    if a < b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


def compare(p1, p2):
    # If both are int just compare them
    if isinstance(p1, int) and isinstance(p2, int):
        return com(p1, p2)
    # Find which one isnt list and turn int to list
    p1 = [p1] if isinstance(p1, int) else p1
    p2 = [p2] if isinstance(p2, int) else p2
    # Get len
    len_part1, len_part2 = len(p1), len(p2)
    smallest_part = min(len_part1, len_part2)
    # Compare lists
    for i in range(smallest_part):
        result = compare(p1[i], p2[i])
        if result == -1:
            return -1
        elif result == 1:
            return 1
    # If we get here that means so far both lists are similar
    # so either both are identical
    # or one list is bigger that the other length wise
    # and we get our answer by sipmply comparing their length
    return com(len_part1, len_part2)


def part1(p):
    index_right_pairs = []
    index_counter = 1
    while p:
        pair = tuple(map(literal_eval, p[:3][:2]))
        p1, p2 = pair
        result = compare(p1, p2)
        if result == 1:
            index_right_pairs.append(index_counter)
        p = p[3:]
        index_counter += 1
    return sum(index_right_pairs)


def part2(p):
    p = [literal_eval(i) for i in p if i != ""]
    p.extend([[[2]], [[6]]])
    sorted_signal = sorted(p, key=cmp_to_key(compare), reverse=True)
    divider1 = sorted_signal.index([[2]]) + 1
    divider2 = sorted_signal.index([[6]]) + 1
    return divider1 * divider2


if __name__ == "__main__":
    main()
