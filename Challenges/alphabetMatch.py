words = input().split()

ans = []
used = []

for i, word in enumerate(words):
    semi_ans = [word]
    if word in used:
        continue
    for ii, w in enumerate(words[i + 1:]):
        if len(word) != len(w):
            continue
        for char in word:
            if char not in w or w.count(char) != word.count(char):
                break
        else:
            semi_ans.append(w)
    if len(semi_ans) > 1:
        ans.append(semi_ans)
        for ww in semi_ans:
            used.append(ww)

print('\n'.join([' '.join(a) for a in ans]))
