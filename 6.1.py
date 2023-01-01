txt_file = open("input.txt", "r")
lines = txt_file.readlines()
for i, line in enumerate(lines):
    for j in range(len(line)):
        letters = set()
        for k in range(4):
            letters.add(line[j+k])
        if len(letters) == 4:
            print(j+4)
            break


