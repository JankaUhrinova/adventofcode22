txt_file = open("input.txt", "r")
lines = txt_file.readlines()

score = 0
appearences = {}
for i, line in enumerate(lines):
    items = set()
    line = line.strip()
    for j in range(len(line)):
        if line[j] not in items:
            items.add(line[j])
            if line[j] not in appearences.keys():
                appearences[line[j]] = 0
            appearences[line[j]] += 1
    if i%3 == 2:
        for key, value in appearences.items():
            if value == 3:
                if key.islower():
                    score += ord(key)-96
                else:
                    score += ord(key)-38
        appearences = {}
        #print(score)

print(score)

