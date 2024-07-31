import io
import sys


_INPUT = """\
100 100 100
Red

"""


def debug_input():

    sys.stdin = io.StringIO(_INPUT)


def main():
    R, G, B = map(int, input().split())
    not_buy = input()

    if not_buy == "Red":
        print(min(G, B))
    elif not_buy == "Green":
        print(min(R, B))
    else:
        print(min(R, G))


if __name__ == "__main__":
    # debug_input()
    main()
