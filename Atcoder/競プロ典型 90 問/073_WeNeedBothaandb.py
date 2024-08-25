import io
import sys

sys.setrecursionlimit(10**9)

_INPUT = """\
7
b a b a b b a
2 1
3 7
3 2
3 4
5 4
4 6

"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    A = 0
    B = 1
    AB = 2
    N = int(input())
    c = list(input().split())
    for i in range(N):
        if c[i] == "a":
            c[i] = A
        else:
            c[i] = B
    MOD = 10**9 + 7
    networks = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        networks[a - 1].append(b - 1)
        networks[b - 1].append(a - 1)

    def dfs(node):
        value = c[node]
        patterns[node][value] = 1
        patterns[node][AB] = 1
        for next_node in networks[node]:
            if next_node in seen:
                continue
            seen.add(next_node)
            dfs(next_node)
            patterns[node][value] *= (
                patterns[next_node][value] + patterns[next_node][AB]
            )
            patterns[node][value] %= MOD
            patterns[node][AB] *= (
                patterns[next_node][A]
                + patterns[next_node][B]
                + 2 * patterns[next_node][AB]
            )
        patterns[node][AB] -= patterns[node][value]
        patterns[node][AB] %= MOD

    patterns = [[0] * 3 for _ in range(N)]  # 0: a, 1: b, 2: ab
    seen = set([0])
    dfs(0)
    print(patterns[0][AB])


if __name__ == "__main__":
    # debug_input()
    main()
