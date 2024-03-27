m, n = input().split('+')

str_num1 = ''
str_num2 = ''

if not 0<= int(m) <=1000000000000 or not 0<= int(n) <=1000000000000:
    exit()

for i in m:
    if i.isdigit():
        if i == '0':
            str_num1 += i
            continue
        elif i == '1':
            str_num1 += '9'
            continue

        str_num1 += str(int(i) - 1)

for i in n:
    if i.isdigit():
        if i == '0':
            str_num2 += i
            continue
        elif i == '1':
            str_num2 += '9'
            continue

        str_num2 += str(int(i) - 1)
print(int(str_num1) + int(str_num2))