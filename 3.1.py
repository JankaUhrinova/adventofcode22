txt_file = open("input.txt", "r")
lines = txt_file.readlines()

score = 0
for i, line in enumerate(lines):
    items = set()
    line = line.strip()
    for j in range(len(line)//2):
        items.add(line[j])
    for j in range(len(line)//2, len(line)):
        if line[j] in items:
            if line[j].islower():
                score += ord(line[j])-96
            else:
                score += ord(line[j])-38
            break
        #print(score)

print(score)

