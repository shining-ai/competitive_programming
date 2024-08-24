import io
import sys

_INPUT = """\
4
1 2 3 3
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    non_zero = 0
    for a in A:
        if a > 0:
            non_zero += 1

    count = 0
    while non_zero > 1:
        count += 1
        A.sort(reverse=True)
        A[0] -= 1
        A[1] -= 1
        non_zero = 0
        for a in A:
            if a > 0:
                non_zero += 1

    print(count)


if __name__ == "__main__":
    # debug_input()
    main()
