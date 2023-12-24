import io
import sys

sys.setrecursionlimit(1 << 20)  # 再帰上限がデフォルトで 1000 なので変更する

def debug_input():
    _INPUT = """\
5 4
1 2
2 3
3 4
3 5

"""

    sys.stdin = io.StringIO(_INPUT)


ans = []


def dfs(pos, net, visited, N):
    visited[pos] = True
    ans.append(pos)

    for i in net[pos]:
        if visited[i] == False:
            dfs(i, net, visited, N)

    if ans[-1] == N:
        return

    ans.pop()


def main():
    N, M = map(int, input().split())
    net = [[] for _ in range(N + 1)]

    for _ in range(M):
        A, B = map(int, input().split())
        net[A].append(B)
        net[B].append(A)

    visited = [False] * (N + 1)

    dfs(1, net, visited, N)

    if visited[N] == False:
        print("The graph is not connected.")
    else:
        for i in ans:
            if i == 0:
                continue
            print(i, end=" ")
            if i == N:
                break
    print()


if __name__ == "__main__":
    # debug_input()
    main()
