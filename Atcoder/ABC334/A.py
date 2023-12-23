import io
import sys


def debug_input():
    _INPUT = """\
334 343

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    B, G = map(int, input().split())

    if B > G:
        print("Bat")
    else:
        print("Glove")


if __name__ == "__main__":
    # debug_input()
    main()
