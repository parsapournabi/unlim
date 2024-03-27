def run(n, m):
    try:
        if not 0 <= n <= 1000000000000 or not 0 <= m <= 1000000000000:
            raise ValueError('Invalid n or m input')

        if ((m - n) + (n * 2)) <= 9:
            return 1
        else:
            return (((m - n) + (n * 2)) // 9) + 1



    except ValueError as v_ex:
        print(v_ex, 'Please try again')

n, m = list(map(int, (input().split())))
print(run(n , m))
