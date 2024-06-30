import io
import sys


def debug_input():
    _INPUT = """\
verticalreading agh



    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    S, T = input().split()

    for w in range(1, len(S)):
        for i in range(w):
            candidate = ""
            while i < len(S):
                candidate += S[i]
                i += w
            if candidate == T:
                print("Yes")
                return
    print("No")



if __name__ == "__main__":
    # debug_input()
    main()
