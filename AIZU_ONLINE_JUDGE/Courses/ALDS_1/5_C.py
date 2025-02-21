import io
import sys
import math


def debug_input():
    _INPUT = """\
2
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())

    def print_point(p):
        print("{:.8f} {:.8f}".format
              (p[0], p[1]))

    def kock(n, p1, p2):
        if n == 0:
            return

        s = [(2 * p1[0] + p2[0]) / 3, (2 * p1[1] + p2[1]) / 3]
        t = [(p1[0] + 2 * p2[0]) / 3, (p1[1] + 2 * p2[1]) / 3]
        u = [((t[0] - s[0]) * math.cos(math.pi / 3) - (t[1] - s[1]) * math.sin(math.pi / 3) + s[0]),
             ((t[0] - s[0]) * math.sin(math.pi / 3) + (t[1] - s[1]) * math.cos(math.pi / 3) + s[1])]
        kock(n - 1, p1, s)
        print_point(s)
        kock(n - 1, s, u)
        print_point(u)
        kock(n - 1, u, t)
        print_point(t)
        kock(n - 1, t, p2)

    print_point([0, 0])
    kock(N, [0, 0], [100, 0])
    print_point([100, 0])


if __name__ == "__main__":
    debug_input()
    main()
