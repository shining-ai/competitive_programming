import io
import sys
from collections import defaultdict

_INPUT = """\
3 3
10
1 2 2
1 1 1
2 1 1 2 2
1 3 2
2 1 1 2 2
2 2 2 3 2
1 2 3
1 2 1
2 1 1 2 2
2 1 1 3 3
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


class UnionFind:
    def __init__(self):
        self.parent = defaultdict(lambda: -1)
        self.rank = defaultdict(int)
        self.color = defaultdict(int)

    def is_root(self, node):
        return self.parent[node] == -1

    def find_root(self, node):
        while not self.is_root(node):
            node = self.parent[node]
        return node

    def union(self, node1, node2):
        root1 = self.find_root(node1)
        root2 = self.find_root(node2)
        if root1 == root2:
            return
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            if self.rank[root1] == self.rank[root2]:
                self.rank[root1] += 1


def main():
    def paint_red(x, y):
        uf.color[(x, y)] = 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if not (1 <= nx <= H and 1 <= ny <= W):
                continue
            if uf.color[(nx, ny)] == 0:
                continue
            uf.union((x, y), (nx, ny))

    def can_arrive(start_x, start_y, goal_x, goal_y):
        if uf.color[(start_x, start_y)] == 0 or uf.color[(goal_x, goal_y)] == 0:
            print("No")
            return
        start_root = uf.find_root((start_x, start_y))
        goal_root = uf.find_root((goal_x, goal_y))
        if start_root == goal_root:
            print("Yes")
        else:
            print("No")

    H, W = map(int, input().split())
    Q = int(input())
    uf = UnionFind()

    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            paint_red(query[1], query[2])
        else:
            can_arrive(query[1], query[2], query[3], query[4])


if __name__ == "__main__":
    # debug_input()
    main()
