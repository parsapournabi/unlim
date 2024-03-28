n = int(input())
commands = [input().split() for i in range(n)]

registers = {'$r1': 100000,
             '$r2': 99996,
             '$r3': 99992,
             '$r4': 99988,
             '$r5': 99984}
stacked = []
address_dict = {'address[100000]': 0,
                'address[99996]': 1,
                'address[99992]': 2,
                'address[99988]': 3,
                'address[99984]': 4}
ans = []


def push(args):
    r = int(registers.get(*args))
    stacked.append(r)


def pop(args):
    registers[args[0]] = stacked[len(stacked) - 1]
    stacked.pop(len(stacked) - 1)


def add(args):
    r1, r2 = args
    source = int(registers.get(r2, r2))
    des = int(registers.get(r1))
    registers[r1] = source + des


def sub(args):
    r1, r2 = args
    source = int(registers.get(r2, r2))
    des = int(registers.get(r1))
    registers[r1] = des - source


def xor(args):
    r1, r2 = args
    source = int(registers.get(r2, r2))
    des = int(registers.get(r1))
    registers[r1] = source ^ des


def mul(args):
    r1, r2 = args
    source = int(registers.get(r2, r2))
    des = int(registers.get(r1))
    registers[r1] = source * des


def mv(args):
    r1, r2 = args
    source = int(registers.get(r2, stacked[address_dict.get(r2)] if address_dict.get(r2) is not None else r2))
    registers[r1] = source


def prt(args):
    ans.append(registers.get('$r2'))


def nop(args):
    return None


def jump(args):
    return 'jump', *args


method_dict = {'push': push,
               'pop': pop,
               'add': add,
               'sub': sub,
               'mul': mul,
               'xor': xor,
               'nop': nop,
               'prt': prt,
               'jump': jump,
               'mv': mv}

for command in commands:
    method = method_dict.get(command[0])
    res = method(command[1:])
print(''.join([chr(a) for a in ans]))
