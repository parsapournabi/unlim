key = input()
n = int(input())

word_list = []
max_idx = 0
idx = 0
ans = []

for i in range(n):
    word = input()
    if key in word:
        word_list.append(word)
        if word.index(key) > max_idx:
            max_idx = word.index(key)
            idx = word_list.index(word)

for words in word_list:
    if words == word_list[idx]:
        ans.append(words)
        continue
    idx_key = words.index(key)
    star_word = ''
    for star in range(max_idx - idx_key):
        star_word += '*'
    star_word += words
    ans.append(star_word)

for an in ans:
    print(an)