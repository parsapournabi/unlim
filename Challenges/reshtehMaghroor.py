n = input()

sets = []

till_here = []

for char in n:
    if char not in till_here:
        till_here.append(char)
        continue
    idx = till_here.index(char) + 1
    sets.append(till_here)
    if idx != len(till_here):
        till_here = till_here[idx:]
    else:
        till_here = []
    till_here.append(char)

if till_here:
    sets.append(till_here)


print(len(max(sets, key=lambda x: len(x))))