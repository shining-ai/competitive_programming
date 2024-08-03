import io
import sys

_INPUT = """\
4
8 2 5 1
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    num_to_index = {}
    for i in range(N):
        num_to_index[A[i]] = i
    A.sort()
    print(num_to_index[A[-2]] + 1)


if __name__ == "__main__":
    # debug_input()
    main()
