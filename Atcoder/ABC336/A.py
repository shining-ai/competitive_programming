import io
import sys


def debug_input():
    _INPUT = """\
1
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    ans = "L"
    ans = ans + "o" * N + "ng"
    print(ans)

if __name__ == "__main__":
    # debug_input()
    main()
