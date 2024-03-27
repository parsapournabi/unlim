# # Python program to Returns the number of arrangements to form 'n'
# def solve(n):
# # Base case
# 	if(n < 0):
# 		return 0
# 	if(n == 0):
# 		return 1
# 	return solve(n-1)+solve(n-3)+solve(n-5)
#
# # This code is contributed by ishankhandelwals.
# print(solve(5))
import sys

sys.setrecursionlimit(15000)


def loop(n, l, res):
    print(n)
    if not l:
        return 0
    if (cl := [c[1] for c in l]).__contains__(n):
        for i in range(len(cl)):
            # print(i)
            if i != n:
                continue
            res.append(i)
            result = loop(l[i][0], l, res)
            # l.pop(i)
            # l = l
    return res


l = [(1, 0), (2, 1), (4, 1), (100, 4), (101, 2), (3, 5)]
res = []
print(loop(1, l, res))
print(res)
