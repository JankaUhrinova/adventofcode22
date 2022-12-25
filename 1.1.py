txt_file = open("input.txt","r")
lines = txt_file.readlines()

m = 0
c = 0

for i, line in enumerate(lines):
    if line == "\n":
        m = max(c,m)
        c = 0
    else:
        c += int(line)

m = max(m,c)
print(m)