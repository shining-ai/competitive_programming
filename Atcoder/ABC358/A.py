import io
import sys


def debug_input():
    _INPUT = """\
CodeQUEEN Land

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    S, T = input().split()
    if S == "AtCoder" and T == "Land":
        print("Yes")
        return
    print("No")


if __name__ == "__main__":
    # debug_input()
    main()
