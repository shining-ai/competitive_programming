import io
import sys


def debug_input():
    _INPUT = """\
SMR

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    S = input()
    for s in S:
        if s == "R":
            print("Yes")
            return
        elif s == "M":
            print("No")
            return


if __name__ == "__main__":
    # debug_input()
    main()
