import io
import sys


_INPUT = """\
4 7 18
2 3 5 1
8 8 1 4

"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)

    for i in range(N):
        X -= A[i]
        Y -= B[i]
        if X < 0 or Y < 0:
            break
    print(i + 1)


if __name__ == "__main__":
    # debug_input()
    main()
