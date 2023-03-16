with open("input.txt", "r") as f:
    lines = f.read()

p1_score = [0, 0]
p2_score = [0, 0]

p1_dict = {
    "A Y": [1, 8], "B Z": [2, 9], "C X": [3, 7],  # Win
    "A X": [4, 4], "B Y": [5, 5], "C Z": [6, 6],  # Tie
    "A Z": [7, 3], "B X": [8, 1], "C Y": [9, 2],  # Lose

    # "rock paper":    [1, 8], "paper scissors": [2, 9], "scissors rock":     [3, 7],     # Win
    # "rock rock":     [4, 4], "paper paper":    [5, 5], "scissors scissors": [6, 6],     # Tie
    # "rock scissors": [7, 3], "paper rock":     [8, 1], "scissors paper":    [9, 2],     # Lose
}

p2_dict = {
    # paper      | scissors     | rock
    "A Z": [1, 8], "B Z": [2, 9], "C Z": [3, 7],  # Win
    # rock       | paper        | scissors
    "A Y": [4, 4], "B Y": [5, 5], "C Y": [6, 6],  # Tie
    # scissors   | rock         | paper
    "A X": [7, 3], "B X": [8, 1], "C X": [9, 2],  # Lose
}

for line in lines.splitlines():
    p1_score = list(map(sum, zip(p1_score, p1_dict[line])))
    p2_score = list(map(sum, zip(p2_score, p2_dict[line])))

print("Part one:", p1_score)
print("Part Two:", p2_score)
