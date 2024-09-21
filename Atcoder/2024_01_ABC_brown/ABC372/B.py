import io
import sys

_INPUT = """\
6
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    M = int(input())
    zero = M % 3
    remain = M - zero
    ans = []
    while remain != 0:
        for i in range(10, 0, -1):
            if 3**i <= remain:
                ans.append(i)
                remain -= 3**i
                break
    for _ in range(zero):
        ans.append(0)

    print(len(ans))
    for i in reversed(ans):
        print(i, end=" ")
    print()


if __name__ == "__main__":
    # debug_input()
    main()
