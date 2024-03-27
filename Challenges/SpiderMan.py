n = int(input())
towers = list(map(int, input().split()))

jump = 0
ans = 0

for i in range(n):
    try:
        ans += 1
        remain_towers = towers[jump:]
        jump += remain_towers[0]
    except:
        print(ans)
        break
else:
    if remain_towers[0] >= len(remain_towers) or remain_towers[0] == towers[-1] and towers[0] != 0:
        print(ans)
    else:
        print('SpiderMan Wasted')
