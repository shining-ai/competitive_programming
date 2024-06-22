import io
import sys


def debug_input():
    _INPUT = """\
3
Aoki
Takahashi
Takahashi
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    S = [input() for _ in range(N)]

    Takahashi_num = 0
    for s in S:
        if s == "Takahashi":
            Takahashi_num += 1
    print(Takahashi_num)


if __name__ == "__main__":
    # debug_input()
    main()
