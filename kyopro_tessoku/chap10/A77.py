import io
import sys


def debug_input():
    _INPUT = """\
7 45
2
7 11 16 20 28 34 38

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))

    def is_ok(x):
        cnt = 0
        prev = 0
        for i_a in A:
            if i_a - prev >= x and L - i_a >= x:
                prev = i_a
                cnt += 1
        if cnt >= K:
            return True
        else:
            return False

    left = 1
    right = 10**9

    while left < right:
        mid = (left + right + 1) // 2
        if not is_ok(mid):
            right = mid - 1
        else:
            left = mid

    print(left)


if __name__ == "__main__":
    # debug_input()
    main()
