students = input().split()

# Define Enemies
for i, st in enumerate(students):
    if i + 3 >= len(students):
        break
    if st + students[i + 3] == '++':
        students[i] = '-'
        students[i + 3] = '-'
    elif st + students[i + 3] == '--':
        students[i] = '+'
        students[i + 3] = '+'
    elif st + students[i + 3] == '??':
        students[i] = '+'
        students[i + 3] = '+'
    elif st + students[i + 3] == '-+' or st + students[i + 3] == '+-':
        pass
    elif st + students[i + 3] == '-?' or st + students[i + 3] == '?-':
        if st == '?':
            students[i] = '+'
        else:
            students[i + 3] = '+'
    elif st + students[i + 3] == '+?' or st + students[i + 3] == '?+':
        if st == '?':
            students[i] = '-'
        else:
            students[i + 3] = '-'

# Define Friends
for i, st in enumerate(students):
    if i + 2 >= len(students):
        break
    if st + students[i + 2] == '-+' or st + students[i + 2] == '+-':
        students[i] = '-'
        students[i + 2] = '-'
print(' '.join(students))
