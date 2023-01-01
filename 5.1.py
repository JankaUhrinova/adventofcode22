txt_file = open("input.txt", "r")
lines = txt_file.readlines()

stacks = [[] for i in range(9)]
for i, line in enumerate(lines):
    s, c = 0, 1
    if line[c] == '1':
        break
    while c <= len(line):
        if line[c] >= 'A' and line[c] <= 'Z':
            stacks[s].append(line[c])
        c += 4
        s += 1

stacks = [list(reversed(stack)) for stack in stacks]
i += 2
while i < len(lines):
    #print(stacks)
    line = lines[i].split()
    amount = int(line[1])
    fr = int(line[3])-1
    to = int(line[5])-1
    move = stacks[fr][-amount:]
    stacks[fr] = stacks[fr][:-amount]
    stacks[to] += reversed(move)
    i += 1


result = ""


for i in range(9):
    result += stacks[i][-1]

print(result)

