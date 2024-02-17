import io
import sys


def debug_input():
    _INPUT = """\
4
5 7 0 3
2 2
4 3
5 2

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    trade = [list(map(int, input().split())) for _ in range(N - 1)]

    for i in range(N-1):
        trade_num = A[i] // trade[i][0]
        A[i+1] += trade_num * trade[i][1]

    print(A[-1])


if __name__ == "__main__":
    # debug_input()
    main()
