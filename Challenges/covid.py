new_st = int(input())
chairs = list(map(int, input().split()))

cnt = 0

for i, chair in enumerate(chairs):
    if i == 0:
        if chair == 0 and chairs[i + 1] == 0:
            cnt += 1
            chairs[i] = 1

    elif i == len(chairs) - 1:
        if chair == 0 and chairs[i - 1] == 0:
            cnt += 1
            chairs[i] = 1

    else:
        if chair == 0 and chairs[i + 1] == 0 and chairs[i - 1] == 0:
            cnt +=1
            chairs[i] = 1
    if cnt >= new_st:
        print('safe')
        break
else:
    print('danger')