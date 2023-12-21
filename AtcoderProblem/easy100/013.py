import io
import sys


def debug_input():
    _INPUT = """\
454 414 444
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    A, B, C = map(int, input().split())

    count = 0
    while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
        A, B, C = (B + C) // 2, (A + C) // 2, (A + B) // 2
        count += 1
        if A == B == C:
            if A % 2 == 0:
                count = -1
            break

    print(count)


if __name__ == "__main__":
    # debug_input()
    main()
