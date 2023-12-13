import io
import math
import sys


def debug_input():
    _INPUT = """\
1 5


    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N!)
def main():
    H, W = map(int, input().split())

    if H == 1 or W == 1:
        ans = 1
    else:
        ans = math.ceil((H * W) / 2)

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
