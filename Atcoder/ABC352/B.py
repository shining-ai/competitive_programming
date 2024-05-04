import io
import sys


def debug_input():
    _INPUT = """\
atcoder
atcoder

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    S = input()
    T = input()
    i = 0

    for s in S:
        while i < len(T) and s != T[i]:
            i += 1
        print(i + 1, end=" ")
        i += 1


if __name__ == "__main__":
    # debug_input()
    main()
