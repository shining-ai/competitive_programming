import io
import sys

_INPUT = """\
4
3 6 9 3
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    left = 0
    right = 1
    ans = 0
    while left < N - 1 and right < N:
        diff = A[right] - A[left]
        while right < N and A[right] - A[right - 1] == diff:
            right += 1
        num = right - left
        ans += (num *(num + 1)) // 2
        ans -= 1
        left = right - 1
    ans += 1
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
