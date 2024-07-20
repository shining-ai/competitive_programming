import io
import sys


_INPUT = """\
2 4
-3 2
1 -2

"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    a_x, a_y = map(int, input().split())
    b_x, b_y = map(int, input().split())
    c_x, c_y = map(int, input().split())

    a_b = (b_x - a_x, b_y - a_y)
    b_c = (c_x - b_x, c_y - b_y)
    c_a = (a_x - c_x, a_y - c_y)

    naiseki_ab_bc = a_b[0] * b_c[0] + a_b[1] * b_c[1]
    naiseki_bc_ca = b_c[0] * c_a[0] + b_c[1] * c_a[1]
    naiseki_ca_ab = c_a[0] * a_b[0] + c_a[1] * a_b[1]

    if naiseki_ab_bc == 0 or naiseki_bc_ca == 0 or naiseki_ca_ab == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # debug_input()
    main()
