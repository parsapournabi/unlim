global n

call_list: list = []


def run():
    try:
        n = int(input())
        if not 1 <= n <= 100:
            raise ValueError(f'Out of range number of n {n}]')
        for i in range(n):
            values = input().split()
            if len(values) != 3:
                raise ValueError(f'length {values} must be 3')
            call = call_func.get(values[0])

            if call == None:
                continue
            call_list.append((call, int(values[1]), int(values[2])))
        for (calls, inp1, inp2) in call_list:
            print(calls(inp1, inp2))
    except ValueError as v_ex:
        print(v_ex, 'Please try again')


def func_fuel(distance, fuel_per_100Km):
    return f'{round(((distance / 100_000) * fuel_per_100Km), 1)}L'


def func_distance(speed, time):
    return f'{round(((speed / 60) * time), 1)}km'


def func_time(distance, speed):
    return f'{round(((distance / 1000) / speed), 1)}h'


def func_speed(distance, time):
    return f'{round(((distance / 1000) / (time / 60)), 1)}km/h'


call_func = {'fuel': func_fuel, 'distance': func_distance, 'time': func_time, 'speed': func_speed}

run()
