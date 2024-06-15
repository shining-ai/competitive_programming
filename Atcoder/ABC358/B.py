import io
import sys


def debug_input():
    _INPUT = """\
10 50000
120190 165111 196897 456895 540000 552614 561627 743796 757613 991216

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, A = map(int, input().split())
    T = list(map(int, input().split()))

    all_time = 0
    for t in T:
        if all_time < t:
            all_time = t
        all_time += A
        print(all_time)


if __name__ == "__main__":
    # debug_input()
    main()
