import io
import sys


def debug_input():
    _INPUT = """\
5
1 2 3 4 5
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = [0] + list(map(int, input().split()))

    left = [0] * (N + 2)
    right = [0] * (N + 2)

    for i in range(1, N + 1):
        left[i] = min(A[i], left[i - 1] + 1)
    for i in range(N, 0, -1):
        right[i] = min(A[i], right[i + 1] + 1)

    ans_list = (min(left[i], right[i]) for i in range(1, N + 1))
    print(max(ans_list))


if __name__ == "__main__":
    debug_input()
    main()
