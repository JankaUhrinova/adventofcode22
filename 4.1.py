import re

txt_file = open("input.txt", "r")
lines = txt_file.readlines()

score = 0
for i, line in enumerate(lines):
    coordinates = re.split(',|-',line.strip())
    coordinates = [int(coordinate) for coordinate in coordinates]
    if coordinates[0] <= coordinates[2] and coordinates[1] >= coordinates[3]:
        score += 1
    elif coordinates[0] >= coordinates[2] and coordinates[1] <= coordinates[3]:
        score += 1

print(score)

