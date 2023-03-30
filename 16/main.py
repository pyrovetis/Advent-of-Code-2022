import itertools
import nographs as nog


def main():
    with open("input.txt", "r") as f:
        puzzle = f.read().splitlines()

    print("Part one:", part1(puzzle))
    print("Part two:", part2(puzzle))


def parse_input(p):
    rates = dict()
    valves = dict()

    for line in p:
        valve = line.split()[1]
        rate = int(line.split(";")[0].split("=")[1])
        targets = line.split("to ")[1].split(" ", 1)[1].split(", ")

        rates[valve] = rate
        valves[valve] = targets

    relevant_valves = frozenset(v for v, r in rates.items() if r != 0)
    max_release = sum(r for v, r in rates.items())

    return rates, valves, max_release, relevant_valves


def part1(p):
    rates, valves, max_release, relevant_valves = parse_input(p)
    limit = 30

    def next_edges(state: tuple[str, frozenset, int], _):
        valve, closed, releasing = state
        if valve in closed:
            yield (valve, closed.difference([valve]), releasing + rates[valve]
                   ), max_release - releasing
        for to_valve in valves[valve]:
            yield (to_valve, closed, releasing), max_release - releasing

    t = nog.TraversalShortestPaths(next_edges)
    for state in t.start_from(("AA", relevant_valves, 0)):
        valve, closed, releasing = state
        if t.depth == limit or not closed:
            return max_release * limit - t.distance


def part2(p):
    rates, valves, max_release, relevant_valves = parse_input(p)
    limit = 26

    def next_edges(state: tuple[str, frozenset, int], _):
        valve, closed, releasing = state
        if valve in closed:
            yield (valve, closed.difference([valve]), releasing + rates[valve]
                   ), max_release - releasing
        for to_valve in valves[valve]:
            yield (to_valve, closed, releasing), max_release - releasing

    def next_edges_we(state: tuple[str, str, frozenset, int], _):
        me, elephant, closed, releasing = state
        for me_next, elephant_next in itertools.product(
                next_edges((me, closed, releasing), _),
                next_edges((elephant, closed, releasing), _)
        ):
            (me_to, me_closed, me_releasing), weight = me_next
            (el_to, el_closed, el_releasing), weight = elephant_next
            if not (me_closed == el_closed and me_closed != closed):
                yield (me_to, el_to, me_closed.intersection(el_closed),
                       releasing + (me_releasing-releasing) +
                       (el_releasing-releasing)
                       ), weight

    t = nog.TraversalShortestPaths(next_edges_we)
    for state in t.start_from(("AA", "AA", relevant_valves, 0)):
        valve, valve_ele, closed, releasing = state
        if t.depth == limit or not closed:
            return max_release * limit - t.distance


if __name__ == "__main__":
    main()
