from math import floor
import numpy as np


def main():
    with open("input.txt", "r") as f:
        puzzle = f.read().splitlines()

        print("Part one:", part1(puzzle))
        print("Part two:", part2(puzzle))


def init_monkey_items(p):
    monkeys = []
    for i in range(8):
        monkey_segment = p[:7]
        items = monkey_segment[1].replace(",", "").split()[2:]
        items = [int(i) for i in items]

        monkeys.append(items)

        p = p[7:]
    return monkeys


def cycle(m, all_monkeys, loop, monkey_inspected, magic_mod=0, p2=False):
    monkey = {
        "number": int(m[0].split()[1][0]),
        "items": all_monkeys[loop],
        "operation": m[2].split()[4],
        "operation_value": m[2].split()[5],
        "test": int(m[3].split()[-1]),
        "test_true": int(m[4].split()[-1]),
        "test_false": int(m[5].split()[-1])
    }

    for _ in range(len(monkey["items"])):
        # Item in the monkey's hands
        current_item = monkey["items"].pop(0)
        # Add monkey inspection list
        monkey_inspected[monkey["number"]].append(current_item)
        # all_monkeys[loop].remove(current_item)
        # Fix operation value
        op_value = int(monkey["operation_value"]) if monkey["operation_value"].isdigit(
        ) else current_item
        # Calculate new stress for item
        match monkey["operation"]:
            case "*":
                current_item = np.multiply(
                    current_item, op_value, dtype=np.int64)
            case "+":
                current_item = np.add(current_item, op_value, dtype=np.int64)
        # Monkey gets bored and drops item (divide by 3)
        if not p2:
            current_item = floor(current_item / 3)
        else:
            current_item = current_item % magic_mod

        if not current_item % monkey["test"]:
            all_monkeys[monkey["test_true"]].append(current_item)
        else:
            all_monkeys[monkey["test_false"]].append(current_item)


def part1(p):
    monkey_inspected = [[] for i in range(8)]
    monkey_items = init_monkey_items(p)
    round_count = 20
    full_puzzle = p
    for i in range(round_count):
        # Read every monkey segment
        for i in range(8):
            monkey_segment = p[:7]

            cycle(monkey_segment, monkey_items, i, monkey_inspected)

            p = p[7:]
        p = full_puzzle

    for index, item in enumerate(monkey_inspected):
        print(f"Monkey {index} inspected items {len(item)} times.")

    monkey_business = sorted([len(i)for i in monkey_inspected], reverse=True)[
        :2][0] * sorted([len(i) for i in monkey_inspected], reverse=True)[:2][1]
    return monkey_business


def all_test_divides(p):
    magic_mod = 1
    for item in p:
        if "Test" in item:
            magic_mod = magic_mod * int(item.split()[-1])
    return magic_mod


def part2(p):
    monkey_inspected = [[] for i in range(8)]
    monkey_items = init_monkey_items(p)
    round_count = 10000
    full_puzzle = p
    magic_mod = all_test_divides(p)

    for i in range(round_count):
        # Read every monkey segment
        for i in range(8):
            monkey_segment = p[:7]

            cycle(monkey_segment, monkey_items, i,
                  monkey_inspected, magic_mod, True)

            p = p[7:]
        p = full_puzzle

    for index, item in enumerate(monkey_inspected):
        print(f"Monkey {index} inspected items {len(item)} times.")

    monkey_business = sorted([len(i)for i in monkey_inspected], reverse=True)[
        :2][0] * sorted([len(i) for i in monkey_inspected], reverse=True)[:2][1]
    return f"{monkey_business:,} | {monkey_business}"


if __name__ == "__main__":
    main()
