import io
import sys


def debug_input():
    _INPUT = """\
2 4
10 20 30 40
20 0 10 30
0 100 100 0

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    X = [list(map(int, input().split())) for _ in range(N)]

    for food in X:
        for i in range(M):
            A[i] -= food[i]

    for a in A:
        if a > 0:
            print("No")
            return
    print("Yes")




if __name__ == "__main__":
    # debug_input()
    main()
