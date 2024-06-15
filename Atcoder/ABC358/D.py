import io
import sys


def debug_input():
    _INPUT = """\
7 3
2 6 8 9 5 1 11
3 5 7

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    amount = 0
    index = 0
    for b in B:
        if index >= N:
            print("-1")
            return
        while A[index] < b:
            index += 1
            if index >= N:
                print("-1")
                return
        amount += A[index]
        index += 1
    print(amount)


if __name__ == "__main__":
    # debug_input()
    main()
