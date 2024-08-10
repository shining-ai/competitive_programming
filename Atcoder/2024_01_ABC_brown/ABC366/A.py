import io
import sys

_INPUT = """\
7 4 2
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, T, A = map(int, input().split())
    if T > (N // 2) or A > (N // 2):
        print("Yes")
        return
    print("No")

if __name__ == "__main__":
    # debug_input()
    main()
