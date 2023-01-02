class folder():
    def __init__(self, name):
        self.kids = []
        self.name = name
        self.size = 0

class file():
    def __init__(self, name, size):
        self.name = name
        self.size = size

track = []
current:folder = None
begin:folder = None
txt_file = open("input.txt", "r")
lines = txt_file.readlines()

for i, line in enumerate(lines):
    line = line.split()
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                track.pop()
                current = track[-1]
                continue

            if current == None:
                current = folder(line[2])
                begin = current

            else:
                for kid in current.kids:
                    if kid.name == line[2] and type(kid) == folder:
                        current = kid
            track.append(current)
    else:
        if line[0] == "dir":
            d = folder(line[1])
        else:
            d = file(line[1], int(line[0]))
        current.kids.append(d)

result = 0
to_free = 10000000000
possible = [] 

def find_size(d):
    global result
    global to_free
    global possible
    if type(d) == file:
        return d.size
    else:
        size = 0
        for kid in d.kids:
            size += find_size(kid)
        if size < 100000:
            result += size
        if size >= to_free:
            possible.append(size)
        return size

root_size = find_size(begin)
print(root_size)
to_free = root_size - 40000000
root_size = find_size(begin)

print(result)
print(sorted(possible)[0])