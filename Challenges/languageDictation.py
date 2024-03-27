key = input()
word, num = input().split()

ans_word = False
ans_num = False

for w in word:
    if word.count(w) > key.count(w):
        break
else:
    ans_word = True
for n in num:
    if num.count(n) > key.count(n):
        break
else:
    ans_num = True
print(ans_word)
print(ans_num)
