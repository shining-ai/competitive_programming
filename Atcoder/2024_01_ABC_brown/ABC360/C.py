import io
import sys
import collections


def debug_input():
    _INPUT = """\
12
3 6 7 4 12 4 8 11 11 1 8 11
3925 9785 9752 3587 4013 1117 3937 7045 6437 6208 3391 6309

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    W = list(map(int, input().split()))

    cost = 0
    box = collections.defaultdict(int)

    for i in range(N):
        cost += min(box[A[i]], W[i])
        box[A[i]] = max(box[A[i]], W[i])

    print(cost)


if __name__ == "__main__":
    # debug_input()
    main()
