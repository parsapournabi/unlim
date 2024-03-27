import sys
from copy import deepcopy

sys.setrecursionlimit(150000)


class Process:
    def __init__(self, ids, child, query):
        self.id = ids
        self.child = child
        self.query = query

    def __repr__(self):
        return f"({self.id}, {self.child}, {self.query})"


n, q = list(map(int, input().split()))

process_list = [Process(*list(map(int, input().split()))) for i in range(n)]
queries_list = [int(input()) for j in range(q)]
# process_list_copy = deepcopy(process_list)

answer = []

for query in queries_list:
    ans = 0
    for process in process_list:
        if process.child != query:
            continue
        ans += process.query
