import io
import sys

_INPUT = """\
5
e869120
atcoder
e869120
square1001
square1001
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    users = set()
    for day in range(1, N + 1):
        user = input()
        if user in users:
            continue
        users.add(user)
        print(day)


if __name__ == "__main__":
    # debug_input()
    main()
