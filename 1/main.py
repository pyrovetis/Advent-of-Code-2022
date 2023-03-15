from itertools import groupby


with open("input.txt", "r") as f:
    lines = f.read().splitlines()

# Split list from empty values
lst = [list(sub) for ele, sub in groupby(lines, key=bool) if ele]
# Str to int
lst = [list(map(int, x)) for x in lst]

# Part 1
print(
    "Part one:",
    max([sum(x) for x in lst])
)
# Part 2
print(
    "Part two:",
    sum(
        sorted(
            [sum(x) for x in lst], reverse=True
        )[:3]  # Get top 3
    )
)
