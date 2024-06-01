import io
import sys


def debug_input():
    _INPUT = """\
10 1 10

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, L, R = map(int, input().split())
    ans = [i for i in range(1, N + 1)]
    while L <= R:
        ans[L - 1], ans[R - 1] = ans[R - 1], ans[L - 1]
        L += 1
        R -= 1
    for i in ans:
        print(i, end=" ")


if __name__ == "__main__":
    # debug_input()
    main()
