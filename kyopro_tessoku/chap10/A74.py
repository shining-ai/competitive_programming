import io
import sys


def debug_input():
    _INPUT = """\
4
0 0 2 0
3 0 0 0
0 0 0 4
0 1 0 0
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    X = [None] * N
    Y = [None] * N

    for i in range(N):
        for j in range(N):
            if A[i][j] != 0:
                X[i] = A[i][j]
                Y[j] = A[i][j]

    def count(Z):
        cnt = 0
        for i in range(N):
            for j in range(i + 1, N):
                if Z[i] > Z[j]:
                    cnt += 1
        return cnt

    print(count(X) + count(Y))


if __name__ == "__main__":
    # debug_input()
    main()
