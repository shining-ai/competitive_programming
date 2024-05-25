import io
import sys


def debug_input():
    _INPUT = """\
3 2
3 2 5
4 1

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = A + B
    C.sort()
    A.sort()
    prev = C.index(A[0])
    for a in A:
        current = C.index(a)
        if current - prev == 1:
            print("Yes")
            return
        prev = current
    print("No")



if __name__ == "__main__":
    # debug_input()
    main()
