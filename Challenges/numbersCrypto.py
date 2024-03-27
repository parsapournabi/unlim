num = input()

used = []
ans = ''
previous = ''
count = 0

for ic, char in enumerate(num):
    # if char not in used:
    #     used.clear()
    #
    #     ans += f'{str(num[ic: ic+].count(char))}{char}'
    #     used.append(char)
    if char != previous:
        if previous != '':
            ans += str(count) + previous
        previous = char
        count = 1
    else:
        count += 1
ans += str(count) + previous

ans = int(ans)
if ans % 2:
    ans = ans * 3
else:
    ans = int(ans / 2)
print(ans)
