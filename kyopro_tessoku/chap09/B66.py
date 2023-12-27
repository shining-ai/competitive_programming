import io
import sys


def debug_input():
    _INPUT = """\
4 3
1 2
2 3
3 4
7
2 1 2
2 1 3
2 1 4
1 2
2 1 2
2 1 3
2 1 4

    """

    sys.stdin = io.StringIO(_INPUT)


class unionfind:
    # n 頂点の Union-Find 木を作成
    # （ここでは頂点番号が 1-indexed になるように実装しているが、0-indexed の場合は par, size のサイズは n でよい）
    def __init__(self, n):
        self.n = n
        self.par = [-1] * (n + 1)  # 最初は親が無い
        self.size = [1] * (n + 1)  # 最初はグループの頂点数が 1

    # 頂点 x の根を返す関数
    def root(self, x):
        # 1 個先（親）がなくなる（つまり根に到達する）まで、1 個先（親）に進み続ける
        while self.par[x] != -1:
            x = self.par[x]
        return x

    # 要素 u, v を統合する関数
    def unite(self, u, v):
        rootu = self.root(u)
        rootv = self.root(v)
        if rootu != rootv:
            # u と v が異なるグループのときのみ処理を行う
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]

    #  要素 u と v が同一のグループかどうかを返す関数
    def same(self, u, v):
        return self.root(u) == self.root(v)


def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(M)]
    edges.insert(0, [0, 0])
    Q = int(input())
    queries = [list(map(int, input().split())) for i in range(Q)]
    queries.insert(0, [0, 0, 0])
    last = [True] * (M + 1)
    last[0] = False
    ans = []

    for i in range(Q + 1):
        if queries[i][0] == 1:
            last[queries[i][1]] = False

    uf = unionfind(N)
    for i in range(1, M + 1):
        if last[i]:
            uf.unite(edges[i][0], edges[i][1])

    for i in reversed(range(1, Q + 1)):
        if queries[i][0] == 1:
            uf.unite(edges[queries[i][1]][0], edges[queries[i][1]][1])
        else:
            ans.append(uf.same(queries[i][1], queries[i][2]))

    for a in reversed(ans):
        if a:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    # debug_input()
    main()
