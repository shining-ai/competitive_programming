import io
import sys


def debug_input():
    _INPUT = """\
7
3 7 2 1 6 5 4
13
2 3
1 2
1 3
3 6
3 7
2 4
3 7
1 3
4 7
1 6
2 4
1 3
1 3

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = int(input())

    hash_map = dict()
    for i, p in enumerate(P):
        hash_map[p] = i + 1

    for _ in range(Q):
        a, b = map(int, input().split())
        if hash_map[a] < hash_map[b]:
            print(a)
            continue
        print(b)


if __name__ == "__main__":
    # debug_input()
    main()
