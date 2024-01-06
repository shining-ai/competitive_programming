import io
import sys


def debug_input():
    _INPUT = """\
    3
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())

    for i_x in range(N + 1):
        for i_y in range(N + 1):
            for i_z in range(N + 1):
                if i_x + i_y + i_z <= N:
                    print(i_x, i_y, i_z)


if __name__ == "__main__":
    # debug_input()
    main()
