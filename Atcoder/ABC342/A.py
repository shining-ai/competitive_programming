import collections
import io
import sys


def debug_input():
    _INPUT = """\
zzzzzwz


    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    S = input()
    counts = collections.defaultdict(int)
    for c in S:
        counts[c] += 1
    for i, c in enumerate(S):
        if counts[c] == 1:
            print(i + 1)
            return


if __name__ == "__main__":
    # debug_input()
    main()
