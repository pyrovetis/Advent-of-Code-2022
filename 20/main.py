def main():
    with open("input.txt", "r") as f:
        puzzle = f.read().splitlines()

    print("Part one:", part1(puzzle))
    print("Part two:", part2(puzzle))


class Node:
    def __init__(self, n):
        self.n = n
        self.left = None
        self.right = None


def part1(p):
    x = [Node(int(x)) for x in p]

    for i in range(len(x)):
        x[i].left = x[(i - 1) % len(x)]
        x[i].right = x[(i + 1) % len(x)]

    mod = len(x) - 1

    for k in x:
        if k.n == 0:
            z = k
            continue
        p = k
        if k.n > 0:
            for _ in range(k.n % mod):
                p = p.right
            if k == p:
                continue
            k.right.left = k.left
            k.left.right = k.right
            p.right.left = k
            k.right = p.right
            p.right = k
            k.left = p
        else:
            for _ in range(-k.n % mod):
                p = p.left
            if k == p:
                continue
            k.left.right = k.right
            k.right.left = k.left
            p.left.right = k
            k.left = p.left
            p.left = k
            k.right = p

    t = 0

    for _ in range(3):
        for _ in range(1000):
            z = z.right
        t += z.n

    return t


def part2(p):
    x = [Node(int(x) * 811589153) for x in p]

    for i in range(len(x)):
        x[i].left = x[(i - 1) % len(x)]
        x[i].right = x[(i + 1) % len(x)]

    mod = len(x) - 1

    for _ in range(10):
        for k in x:
            if k.n == 0:
                z = k
                continue
            p = k
            if k.n > 0:
                for _ in range(k.n % mod):
                    p = p.right
                if k == p:
                    continue
                k.right.left = k.left
                k.left.right = k.right
                p.right.left = k
                k.right = p.right
                p.right = k
                k.left = p
            else:
                for _ in range(-k.n % mod):
                    p = p.left
                if k == p:
                    continue
                k.left.right = k.right
                k.right.left = k.left
                p.left.right = k
                k.left = p.left
                p.left = k
                k.right = p

    t = 0

    for _ in range(3):
        for _ in range(1000):
            z = z.right
        t += z.n

    return t


if __name__ == "__main__":
    main()
