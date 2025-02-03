import io
import sys
import bisect


def debug_input():
    _INPUT = """\
5
1 2 3 4 5
3
3 4 1
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))
    S.sort()
    count = 0
    for t_val in T:
        index = bisect.bisect_left(S, t_val)
        if S[index] == t_val:
            count += 1
    print(count)


if __name__ == "__main__":
    # debug_input()
    main()
