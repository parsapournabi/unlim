username = input()

for char in username:
    if username.count(char) < 2:
        print('not cool')
        break
else:
    print('cool')
