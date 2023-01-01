txt_file = open("input.txt", "r")
lines = txt_file.readlines()
for i, line in enumerate(lines):
    for j in range(len(line)):
        letters = set()
        for k in range(14):
            letters.add(line[j+k])
        if len(letters) == 14:
            print(j+14)
            break


