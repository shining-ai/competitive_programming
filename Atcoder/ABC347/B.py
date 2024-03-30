import io
import sys


def debug_input():
    _INPUT = """\
abracadabra
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    S = input()
    sub = set()
    for i in range(len(S)):
        for j in range(i + 1, len(S) + 1):
            sub.add(S[i:j])
    print(len(sub))


if __name__ == "__main__":
    # debug_input()
    main()
