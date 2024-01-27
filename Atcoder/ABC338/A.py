import io
import sys


def debug_input():
    _INPUT = """\
A

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    S = input()
    for i in range(len(S)):
        if i == 0:
            if not S[i].isupper():
                print("No")
                return
        else:
            if not S[i].islower():
                print("No")
                return

    print("Yes")


if __name__ == "__main__":
    # debug_input()
    main()
