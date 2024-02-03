import io
import sys


def debug_input():
    _INPUT = """\
atcoder.jp
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    S = input()
    for i in reversed(range(len(S))):
        if S[i] == ".":
            break

    print(S[i + 1 :])


if __name__ == "__main__":
    # debug_input()
    main()
