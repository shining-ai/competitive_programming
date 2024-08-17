import io
import sys

_INPUT = """\
21 8 14
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    shout, start, end = map(int, input().split())
    if start > end:
        if start <= shout <= 24:
            print("No")
            return
        if 0 <= shout < end:
            print("No")
            return
        print("Yes")
        return

    if start <= shout < end:
        print("No")
        return
    print("Yes")


if __name__ == "__main__":
    # debug_input()
    main()
