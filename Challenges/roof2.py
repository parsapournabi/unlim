# import time
# from random import randint
#
# n, m = list(map(int, input().split()))
# t = []
#
# for i in range(n):
#     towers = list(map(int, input().split()))
#     # towers = [randint(10, 99) for ii in range(m)]
#     for tower in towers:
#         t.append(tower)
#
# st = time.time()
#
# ans = list(map(lambda i: next((str(j) for j in t[i:] if j > t[i]), '-1'), range(len(t))))
#
# print(' '.join(ans))
# fn = time.time()
# print(fn - st)
import time
from random import randint
from threading import Thread

answer = []


def process_tower(start, end, t):
    ans = []
    print(start, end, len(t))
    for i in range(start, end):
        next_tower = next((j for j in t[i:] if j > t[i]), '-1')
        ans.append(str(next_tower))
    answer.append(ans)
    return ans


def main():
    n, m = list(map(int, input().split()))
    t = []

    for i in range(n):
        # towers = list(map(int, input().split()))
        towers = [randint(10, 99) for ii in range(m)]
        for tower in towers:
            t.append(tower)

    st = time.time()

    # Divide the list into 3 parts
    mid1 = n * m // 3
    mid2 = mid1 * 2

    # Create 3 threads
    thread1 = Thread(target=process_tower, args=(0, mid1, t))
    thread2 = Thread(target=process_tower, args=(mid1, mid2, t))
    thread3 = Thread(target=process_tower, args=(mid2, n * m, t))

    # Start the threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for all threads to finish
    thread1.join()
    thread2.join()
    thread3.join()

    # Combine the results from the 3 threads
    ans = [' '.join(a) for a in answer]

    print(' '.join(ans))
    fn = time.time()
    print(fn - st)


if __name__ == "__main__":
    main()
