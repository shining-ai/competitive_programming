import io
import sys

_INPUT = """\
2 3
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    H, W = map(int, input().split())
    if H == 1 or W == 1:
        print(H * W)
        return
    max_light = ((H + 1) // 2) * ((W + 1) // 2)
    print(max_light)


if __name__ == "__main__":
    # debug_input()
    main()
