import io
import sys

_INPUT = """\
.v.
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    S = input()
    print(S.replace(".", ""))

if __name__ == "__main__":
    # debug_input()
    main()
