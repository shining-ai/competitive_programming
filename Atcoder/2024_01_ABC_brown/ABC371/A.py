import io
import sys

_INPUT = """\
< < <
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    S = input().split()
    A = 0
    B = 0
    C = 0
    if S[0] == "<":
        B += 1
    else:
        A += 1

    if S[1] == "<":
        C += 1
    else:
        A += 1

    if S[2] == "<":
        C += 1
    else:
        B += 1

    if A == 1:
        print("A")
    elif B == 1:
        print("B")
    else:
        print("C")


if __name__ == "__main__":
    # debug_input()
    main()
