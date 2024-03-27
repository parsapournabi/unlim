n = int(input())
words = [input() for i in range(n)]

chars = 'abcdefghijklmnopqrstuvwxyz'
mc = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
      ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

same = []

for word in words:
    mc_same = ''
    for char in word:
        mc_same += mc[chars.index(char)]
    if mc_same not in same:
        same.append(mc_same)

print(len(same))
