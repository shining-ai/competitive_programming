import io
import sys


def debug_input():
    _INPUT = """\
        5


    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    binary = bin(N)
    ans = 0

    while binary[-1] == "0":
        ans += 1
        binary = binary[:-1]

    print(ans)


if __name__ == "__main__":
    debug_input()
    main()
