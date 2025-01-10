n = int(input())

commands = [input().split() for _ in range(n)]

registers = {f"R{i}": 0 for i in range(16)}
row = 0  # default starts at 1
locks = set()


def SET(X, Y):
    global registers
    global locks
    if not all(char.isdigit() for char in Y):
        Y = registers[Y]
    else:
        Y = int(Y)
    if X not in locks:
        registers[X] = Y


def ADD(X, Y):
    global registers
    if not all(char.isdigit() for char in Y):
        Y = registers[Y]
    else:
        Y = int(Y)
    registers[X] += Y


def SUB(X, Y):
    global registers
    if not all(char.isdigit() for char in Y):
        Y = registers[Y]
    else:
        Y = int(Y)
    registers[X] -= Y
    if registers[X] < 0:
        registers[X] = 0


def XOR(X, Y):
    global registers
    if not all(char.isdigit() for char in Y):
        Y = registers[Y]
    else:
        Y = int(Y)
    registers[X] ^= Y


def IFGTE(X, Y, Z):
    global registers
    global row
    if not all(char.isdigit() for char in Y):
        Y = registers[Y]
    else:
        Y = int(Y)
    if registers[X] >= Y:
        row = int(Z) - 2


def TOGGLE(X):
    global locks
    if X in locks:
        locks.remove(X)
    else:
        locks.add(X)


def SWAP(X, Y):
    global registers
    registers[X], registers[Y] = registers[Y], registers[X]


def PRINT(X):
    print(registers[X])


dict_method = {"SET": SET, "ADD": ADD, "SUB": SUB, "XOR": XOR, "IFGTE": IFGTE, "TOGGLE": TOGGLE, "SWAP": SWAP,
                "PRINT": PRINT}

while row < n:
    cmd = commands[row]
    method = dict_method[cmd[0]]
    args = cmd[1:]
    method(*args)
    row += 1
