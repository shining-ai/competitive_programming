import io
import sys

sys.setrecursionlimit(1 << 20)  # 再帰上限がデフォルトで 1000 なので変更する


def debug_input():
    _INPUT = """\
9
1 2
2 3
2 4
2 5
1 6
6 7
7 8
7 9
    """

    sys.stdin = io.StringIO(_INPUT)


cnt = 0


def dfs(pos, net, visited):
    global cnt
    visited[pos] = True

    for i in net[pos]:
        if visited[i] == False:
            cnt += 1
            dfs(i, net, visited)


def main():
    N = int(input())
    net = [[] for _ in range(N + 1)]
    ans = []

    for _ in range(N - 1):
        A, B = map(int, input().split())
        net[A].append(B)
        net[B].append(A)

    if len(net[1]) == 1:
        print(1)
    else:
        visited = [False] * (N + 1)
        visited[1] = True

        for i in net[1]:
            global cnt
            dfs(i, net, visited)
            ans.append(cnt + 1)
            cnt = 0

        print(sum(ans) - max(ans) + 1)


if __name__ == "__main__":
    # debug_input()
    main()
