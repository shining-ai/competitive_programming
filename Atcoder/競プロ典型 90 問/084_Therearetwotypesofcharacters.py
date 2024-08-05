import io
import sys

_INPUT = """\
4
ooxo
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    S = input()
    pair_num = 0
    left = 0
    for right in range(N):
        while S[left] != S[right]:
            pair_num += N - right
            left += 1
    print(pair_num)


if __name__ == "__main__":
    # debug_input()
    main()
