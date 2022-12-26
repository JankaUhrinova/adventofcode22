txt_file = open("input.txt", "r")
lines = txt_file.readlines()

scores = {"A":1, "B":2, "C":3}
score = 0

for i, line in enumerate(lines):
    letters = line.split()
    if letters[1] == 'X':
        if letters[0] == 'C':
            score +=  2
        elif letters[0] == 'A':
            score += 3
        else: 
            score += 1
    elif letters[1] == 'Y':
        score += scores[letters[0]] + 3
    else:
        score += 6
        if letters[0] == 'B':
            score +=  3
        elif letters[0] == 'C':
            score += 1
        else:
            score += 2


print(score)

