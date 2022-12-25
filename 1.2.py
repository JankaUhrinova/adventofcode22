txt_file = open("input.txt","r")
lines = txt_file.readlines()

m = []
c = 0

for i, line in enumerate(lines):
    if line == "\n":
        m.append(c)
        c = 0
    else:
        c += int(line)

m.append(c)
m = sorted(m)[-3:]
print(m)
m = sum(m)
print(m)