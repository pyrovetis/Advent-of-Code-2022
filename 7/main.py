from collections import defaultdict


def main():
    with open("input.txt", "r") as f:
        puzzle = f.read()

    print("part one:", part1(puzzle))
    print("part two:", part2(puzzle))


def part1(p):
    p = p.splitlines()
    sizes = defaultdict(int)
    stack = []
    answer = 0

    for line in p:
        if line.startswith("$ cd"):
            match line:
                case "$ cd /":
                    stack.clear()
                    stack.append("/")
                case "$ cd ..":
                    stack.pop()
                case _:
                    file_name = line.split()[-1]
                    stack.append(file_name)
        else:
            line = line.split()[0]
            if line.isdigit():
                for i, v in enumerate(stack):
                    temp_dir = '/'.join(stack[:i+1]).replace("//", "/")
                    sizes[temp_dir] += int(line)

    for _, size in sizes.items():
        if size < 100000:
            answer += size

    return answer


def part2(p):
    p = p.splitlines()
    sizes = defaultdict(int)
    stack = []

    for line in p:
        if line.startswith("$ cd"):
            match line:
                case "$ cd /":
                    stack.clear()
                    stack.append("/")
                case "$ cd ..":
                    stack.pop()
                case _:
                    file_name = line.split()[-1]
                    stack.append(file_name)
        else:
            line = line.split()[0]
            if line.isdigit():
                for i, v in enumerate(stack):
                    temp_dir = '/'.join(stack[:i+1]).replace("//", "/")
                    sizes[temp_dir] += int(line)

    size_needed = sizes["/"] + 30000000 - 70000000

    return min([i for i in sizes.values() if i > size_needed])


if __name__ == "__main__":
    main()
