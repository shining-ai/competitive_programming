import io
import sys


def debug_input():
    _INPUT = """\
<>>
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    S = input()
    if S[0] == "<" and S[-1] == ">":
        for i in range(1, len(S) - 1):
            if S[i] == "=":
                continue
            else:
                print("No")
                return
        print("Yes")
        return
    print("No")


if __name__ == "__main__":
    # debug_input()
    main()
