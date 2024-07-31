import io
import sys


def debug_input():
    _INPUT = """\
EC
CA

    """

    sys.stdin = io.StringIO(_INPUT)


def abs_ord(S):
    tmp = abs(ord(S[0]) - ord(S[1]))

    if tmp == 1 or tmp == 4:
        return 1
    else:
        return 0


def main():
    S = input()
    T = input()

    S_value = abs_ord(S)
    T_value = abs_ord(T)


    if S_value == T_value:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # debug_input()
    main()
