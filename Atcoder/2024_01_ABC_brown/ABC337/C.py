import heapq
import io
import sys


def debug_input():
    _INPUT = """\
        6
4 1 -1 5 3 2
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    my_map = {}

    for i, i_a in enumerate(A):
        my_map[i_a] = i + 1

    curr = -1

    for _ in range(N):
        print(my_map[curr], end=" ")
        curr = my_map[curr]

    print()


if __name__ == "__main__":
    # debug_input()
    main()
