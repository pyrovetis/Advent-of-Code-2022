with open("input.txt", "r") as f:
    lines = f.read().splitlines()

duplicates = []
score = 0

while len(lines):
    lst = lines[:3]
    lines = lines[3:]
    duplicates.append(set.intersection(set(lst[0]), set(lst[1]), set(lst[2])))

for letter in duplicates:
    letter = letter.pop()
    ascii = 96 if letter.islower() else 38
    score += ord(letter) - ascii

print("Part two:", score)
