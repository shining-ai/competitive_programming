import io
import sys


def debug_input():
    _INPUT = """\
1 1
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    A, B = map(int, input().split())
    if A == B:
        print(-1)
        return
    candidate = [1, 2, 3]
    candidate.remove(A)
    candidate.remove(B)
    print(candidate[0])


if __name__ == "__main__":
    # debug_input()
    main()
