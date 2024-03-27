game_map: list = [[i + j for j in range(1, 10)] for i in range(0, 100, 10)]


def run():
    n, m = list(map(int, input().split()))
    moves = input()

    y, x = n - 1, m - 1

    cur_map = game_map[y][x]

    for move in moves:
        func = move_dict.get(move)
        y, x = func(x, y)
        cur_map = game_map[y][x]
    print(cur_map)


def m_up(x, y):
    y -= 1
    if y < 0:
        y = len(game_map) - 1

    return y, x


def m_down(x, y):
    y += 1
    if y > len(game_map) - 1:
        y = 0

    return y, x


def m_right(x, y):
    x += 1
    if x > len(game_map[y]) - 1:
        x = 0

    return y, x


def m_left(x, y):
    x -= 1
    if x < 0:
        x = len(game_map[y]) - 1

    return y, x


move_dict = {'U': m_up, 'D': m_down, 'R': m_right, 'L': m_left}
run()
