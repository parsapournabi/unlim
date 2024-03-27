students = []
call_list = []


def run():
    n = int(input())

    for i in range(n):
        query_list = input().split()
        call = call_fun.get(query_list[0])
        if query_list[0] == 'add':
            name = query_list[1]
            month, day = query_list[2].split('/')
            call_list.append((call, (name, int(month), int(day))))

        elif query_list[0] == 'remove':
            call_list.append((call, query_list[1]))

        elif query_list[0] == 'check':
            call_list.append((call))
        elif query_list[0] == 'get_id':
            call_list.append((call, query_list[1]))
    for caller in call_list:
        try:
            if len(caller) > 1:
                caller[0](caller[1])
        except:
            caller()


def func_add(data):
    name, month, day = data
    if name in students or not 4 <= month <= 6 or not 0 <= day <= 31:
        print(f'{name} already exists or time is over')
    else:
        students.append(f'{name} ({month}/{day})')
        print(f'{name} added to list')


def func_remove(name):
    for i, student in enumerate(students):
        if name in student:
            students.pop(i)
            print(f'{name} removed')
            break
    else:
        print(f'{name} is not in list')


def func_check():
    for i, student in enumerate(students):
        print(f'{i + 1} : {student}')


def func_get_id(Id):
    try:
        print(f'id {Id} is {students[int(Id) - 1].split()[0]}')
    except:
        print('no username with this id')


call_fun = {'add': func_add, 'remove': func_remove, 'check': func_check, 'get_id': func_get_id}
run()
