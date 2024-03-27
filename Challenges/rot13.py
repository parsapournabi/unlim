english_chars = 'abcdefghijklmnopqrstuvwxyz'

word = input()
ans = ''
for char in word:
    idx = english_chars.index(char.lower())
    if idx + 13 > 25:
        idx = (idx + 13) - 26
    else:
        idx += 13
    if char.isupper():
        ans += english_chars[idx].upper()
    else:
        ans += english_chars[idx]
print(ans)
