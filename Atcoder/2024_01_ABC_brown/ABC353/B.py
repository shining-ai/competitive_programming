import io
import sys


def debug_input():
    _INPUT = """\
15 100
73 8 55 26 97 48 37 47 35 55 5 17 62 2 60

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    count = 0
    ride = 0
    for a in A:
        if ride + a <= K:
            ride += a
        else:
            ride = a
            count += 1
    if ride > 0:
        count += 1

    print(count)


if __name__ == "__main__":
    # debug_input()
    main()
