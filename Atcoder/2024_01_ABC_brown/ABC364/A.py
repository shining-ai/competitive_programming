import io
import sys


_INPUT = """\
5
salty
sweet
salty
salty
sweet
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    prev = ""
    for i in range(N):
        s = input()
        if prev == "sweet" and s == "sweet":
            break
        prev = s
    if i == N - 1:
        print("Yes")
        return
    print("No")


if __name__ == "__main__":
    # debug_input()
    main()
