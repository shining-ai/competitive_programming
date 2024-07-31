import io
import sys


def debug_input():
    _INPUT = """\
4
-1 1000000000 1000000000 1000000000

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum_value = 0
    min_value = A[0]
    for a in A:
        sum_value += a
        if sum_value < min_value:
            min_value = sum_value

    if min_value >= 0:
        print(sum_value)
        return
    ans = sum_value + abs(min_value)
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
