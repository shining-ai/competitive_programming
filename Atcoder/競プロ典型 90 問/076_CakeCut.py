import io
import sys

_INPUT = """\
3
1 18 1
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    whole_size = sum(A)
    two_A = A + A[:-1]
    size = 0
    left = 0
    right = 0

    for right in range(2 * N - 1):
        size += two_A[right]
        while size > whole_size / 10:
            size -= two_A[left]
            left += 1
        if size == whole_size / 10:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    # debug_input()
    main()
