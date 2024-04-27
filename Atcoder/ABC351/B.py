import io
import sys


def debug_input():
    _INPUT = """\
1
f
q

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = [input() for _ in range(N)]
    B = [input() for _ in range(N)]

    for i in range(N):
        cnt = 0
        for a, b in zip(A[i], B[i]):
            cnt += 1
            if a != b:
                print(i + 1, cnt)


if __name__ == "__main__":
    # debug_input()
    main()
