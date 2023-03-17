with open("input.txt", "r") as f:
    lines = f.read()

duplicates = []
score = 0
a = []

# Split lines into 2
for line in lines.splitlines():
    first, last = set(line[:len(line)//2]), set(line[len(line)//2:])
    duplicates.append("".join(first.intersection(last)))

# Count duplicates between duplicate lists
for letter in duplicates:
    ascii = 96 if letter.islower() else 38
    score += ord(letter) - ascii

print("Part one:", score)
