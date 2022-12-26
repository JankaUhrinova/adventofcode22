txt_file = open("input.txt", "r")
lines = txt_file.readlines()

scores = {"A":1, "B":2, "C":3}
score = 0

for i, line in enumerate(lines):
    letters = line.split()
    score += scores[letters[0]]
    letters[0] = ord(letters[0])-65
    letters[1] = ord(letters[1])-88
    if letters[0] > letters[1]:
        score += 6
    elif letters[0] == letters[1]:
        score += 3

print(score)

