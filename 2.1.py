txt_file = open("input.txt", "r")
lines = txt_file.readlines()

scores = {"X":1, "Y":2, "Z":3}
score = 0

for i, line in enumerate(lines):
    letters = line.split()
    score += scores[letters[1]]
    if letters[1] == 'X':
        if letters[0] == 'C':
            score +=  6
        if letters[0] == 'A':
            score += 3
    elif letters[1] == 'Y':
        if letters[0] == 'A':
            score +=  6
        if letters[0] == 'B':
            score += 3
    else:
        if letters[0] == 'B':
            score +=  6
        if letters[0] == 'C':
            score += 3

print(score)

