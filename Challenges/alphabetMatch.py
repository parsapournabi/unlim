words = input().split()

ans = []

for iw, word in enumerate(words):
    inside = []
    for iiw, w in enumerate(words):
        if iiw == iw or len(w) != len(word):
            continue
        for char, c in zip(word, w):
            if char not in w or c not in word:
                break
        else:
            if word not in ' '.join(ans) and w not in ' '.join(ans):
                inside.append(w)
    if inside:
            ans.append(f'{word} {" ".join([i for i in inside])}')

print('\n'.join(ans))

