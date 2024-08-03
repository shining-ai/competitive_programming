import io
import sys

_INPUT = """\
4 8
1 3 2 4
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    rest = M
    max_give = M // N
    for i, a in enumerate(A):
        give = rest // (N - i)
        max_give = max(max_give, give)
        rest -= a
        if rest <= 0:
            break
    if max_give >= A[-1]:
        print("infinite")
    else:
        print(max_give)

    # cumulative = [0] * (N + 1)
    # for i in range(N):
    #     cumulative[i + 1] = cumulative[i] + A[i]

    # def check(max_give):

    # left = 0
    # right = M
    # while left < right:
    #     mid = (left + right) // 2
    #     if check(mid):
    #         right = mid
    #     else:
    #         left = mid + 1


if __name__ == "__main__":
    # debug_input()
    main()
