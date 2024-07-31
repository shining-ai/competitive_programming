import io
import sys


def debug_input():
    _INPUT = """\
    5 3 -1 6
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    A, M, L, R = map(int, input().split())

    L_p = L - A
    R_p = R - A

    r_t = R_p // M
    l_t = (L_p - 1) // M

    ans = r_t - l_t

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
