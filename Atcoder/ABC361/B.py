import io
import sys


_INPUT = """\
0 0 0 1000 1000 1000
10 10 10 100 100 100

"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    a, b, c, d, e, f = map(int, input().split())
    g, h, i, j, k, l = map(int, input().split())

    x_small = min(a, d)
    x_big = max(a, d)
    y_small = min(b, e)
    y_big = max(b, e)
    z_small = min(c, f)
    z_big = max(c, f)

    if max(g, j) <= x_small or x_big <= min(g, j):
        print("No")
        return
    if max(h, k) <= y_small or y_big <= min(h, k):
        print("No")
        return
    if max(i, l) <= z_small or z_big <= min(i, l):
        print("No")
        return
    print("Yes")


if __name__ == "__main__":
    # debug_input()
    main()
