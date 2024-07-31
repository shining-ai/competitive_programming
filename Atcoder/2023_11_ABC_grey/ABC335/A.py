import io
import sys


def debug_input():
    _INPUT = """\
hello2023

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    S = input()

    print(S[:-1] + "4")


if __name__ == "__main__":
    debug_input()
    main()
