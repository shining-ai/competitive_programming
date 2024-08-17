import io
import sys

_INPUT = """\
99.900
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    X = str(input())
    for i in range(len(X)-1, -1, -1):
        if X[i] == "0":
            continue
        elif X[i] == ".":
            i -= 1
            break
        else:
            break

    print(X[:i+1])


if __name__ == "__main__":
    # debug_input()
    main()
