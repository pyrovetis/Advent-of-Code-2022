import sympy


def main():
    with open("input.txt", "r") as f:
        puzzle = f.read().splitlines()

    print("Part one:", part1(puzzle))
    print("Part two:", part2(puzzle))


def part1(p):
    monkeys = {}

    for a in p:
        name, expr = a.split(": ")
        if expr.isdigit():
            monkeys[name] = int(expr)
        else:
            left, op, right = expr.split()
            if left in monkeys and right in monkeys:
                monkeys[name] = eval(f"{monkeys[left]} {op} {monkeys[right]}")
            else:
                p.append(a)

    return int(monkeys["root"])


def part2(p):
    monkeys = {"humn": sympy.Symbol("x")}
    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    for a in p:
        name, expr = a.split(": ")
        if name in monkeys:
            continue
        if expr.isdigit():
            monkeys[name] = sympy.Integer(expr)
        else:
            left, op, right = expr.split()
            if left in monkeys and right in monkeys:
                if name == "root":
                    r = sympy.solve(monkeys[left] - monkeys[right])
                    break
                monkeys[name] = ops[op](monkeys[left], monkeys[right])
            else:
                p.append(a)

    return r[0]


if __name__ == "__main__":
    main()
