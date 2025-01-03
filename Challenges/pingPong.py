n, k = list(map(int, input().split()))
rounds = input()


def get_winner(r, maximum):
    players = {'A': "Ali",
               'R': "Reza"
    }
    for player in r:
        if r.count(player) == maximum:
            print(players[player])
            exit()


ali_win_count = rounds.count('A')
reza_win_count = rounds.count('R')
min_win = min(ali_win_count, reza_win_count)
max_win = max(ali_win_count, reza_win_count)

diff_win = max_win - min_win

remain = n - k

if remain < diff_win:
    get_winner(rounds, max_win)
else:
    print('Mobham')
