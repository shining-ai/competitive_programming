import io
import sys

_INPUT = """\
99999 1000000000000000000
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())
    visited = [-1] * (10**5)

    def push_a(x):
        y = 0
        for c in str(x):
            y += int(c)
        z = (x + y) % (10**5)
        return z

    x = N
    for i in range(K):
        if visited[x] != -1:
            cycle = i - visited[x]
            remain = (K - i) % cycle
            break
        visited[x] = i
        x = push_a(x)
    else:
        print(x)
        return

    for i in range(remain):
        x = push_a(x)
    print(x)


if __name__ == "__main__":
    # debug_input()
    main()
