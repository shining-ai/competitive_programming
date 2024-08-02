import io
import sys

_INPUT = """\
2 5
1 3
2 1
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    need_to_change = 0
    for i in range(N):
        need_to_change += abs(A[i] - B[i])
    if need_to_change <= K and (K - need_to_change) % 2 == 0:
        print("Yes")
        return
    print("No")


if __name__ == "__main__":
    # debug_input()
    main()
