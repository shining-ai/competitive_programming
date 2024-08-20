import io
import sys
from collections import defaultdict

_INPUT = """\
4
7
0 1 2 3
1 1 2 1
1 3 4 5
0 3 4 6
1 3 4 5
0 2 3 6
1 3 1 5
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


class UnionFind:
    def __init__(self, n):
        self.parent = defaultdict(lambda: -1)
        self.rank = defaultdict(int)

    def is_root(self, node):
        return self.parent[node] == -1

    def find(self, node):
        root = node
        while not self.is_root(root):
            root = self.parent[root]
        # 経路圧縮
        while node != root:
            parent = self.parent[node]
            self.parent[node] = root
            node = parent
        return root

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return
        if self.rank[root1] < self.rank[root2]:
            smaller, bigger = root2, root1
        else:
            smaller, bigger = root1, root2
        self.parent[smaller] = bigger
        self.rank[bigger] = max(self.rank[bigger], self.rank[smaller] + 1)


def main():
    N = int(input())
    Q = int(input())
    union_find = UnionFind(N)
    query = []
    for _ in range(Q):
        T, X, Y, V = map(int, input().split())
        query.append((T, X, Y, V))

    relation = [0] * (N + 1)
    for T, X, Y, V in query:
        if T == 1:
            continue
        relation[Y] = V

    # A[0] = 0としたときの値
    A = [0] * (N + 1)
    for i in range(1, N + 1):
        A[i] = relation[i] - A[i - 1]

    for T, X, Y, V in query:
        if T == 0:
            union_find.union(X, Y)
            continue
        if not (union_find.find(X) == union_find.find(Y)):
            print("Ambiguous")
            continue
        different = V - A[X]
        if (X + Y) % 2 == 1:
            different *= -1
        print(A[Y] + different)


if __name__ == "__main__":
    # debug_input()
    main()
