import io
import sys


def debug_input():
    _INPUT = """\
5 4
1 2
2 3
3 4
3 5
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M = map(int, input().split())
    result = [set() for _ in range(N + 1)]
    max_len = 0
    ans = 0

    for _ in range(M):
        A, B = map(int, input().split())
        result[A].add(B)
        result[B].add(A)

    for i in range(1, N + 1):
        if max_len < len(result[i]):
            max_len = len(result[i])
            ans = i

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
