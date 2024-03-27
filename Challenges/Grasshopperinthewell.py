height, jump = list(map(float, input().split()))

fall = 1.0
count = 0.0
failed = -1.0
j = 0

while True:
    count += jump
    j += 1
    if count >= height:
        print(f'Azadi ba {j} paresh')
        break
    count -= fall
    fall += 0.2
    if failed >= count:
        print('Malakh failed')
        break
    failed = count