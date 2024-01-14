import io
import sys


def debug_input():
    _INPUT = """\
133
    """

    sys.stdin = io.StringIO(_INPUT)


import numpy as np


def main():
    N = int(input())
    nums = [0, 2, 4, 6, 8]
    quintal_num = np.base_repr(N - 1, 5)

    for i in str(quintal_num):
        print(nums[int(i)], end="")

    print()


if __name__ == "__main__":
    # debug_input()
    main()
