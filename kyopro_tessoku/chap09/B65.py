import io
import sys

sys.setrecursionlimit(1 << 30)  # 再帰上限をなくす


def debug_input():
    _INPUT = """\
15 1
1 2
2 3
1 4
1 5
1 6
6 7
2 8
6 9
9 10
10 11
6 12
12 13
13 14
12 15
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, T = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(N - 1)]
    rank = [-1] * (N + 1)

    # 隣接リスト
    net = [[] for _ in range(N + 1)]
    for a, b in edges:
        net[a].append(b)
        net[b].append(a)

    def dfs(boss, person):
        for i in net[person]:
            if i == boss:
                if len(net[person]) == 1:
                    rank[person] = 0
                continue
            dfs(person, i)
            rank[person] = max(rank[person], rank[i] + 1)

    dfs(0, T)

    for i in range(1, N + 1):
        print(rank[i], end=" ")

    print()


if __name__ == "__main__":
    # debug_input()
    main()
