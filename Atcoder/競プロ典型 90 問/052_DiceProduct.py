import io
import sys

_INPUT = """\
2
1 2 3 5 7 11
4 6 8 9 10 12
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    sum_all_volume = 1
    for _ in range(N):
        A = list(map(int, input().split()))
        sum_all_volume *= sum(A)
        sum_all_volume %= 10**9 + 7
    print(int(sum_all_volume) % (10**9 + 7))


if __name__ == "__main__":
    # debug_input()
    main()
