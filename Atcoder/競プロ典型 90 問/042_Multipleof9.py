import io
import sys

_INPUT = """\
1
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    K = int(input())
    if K % 9 != 0:
        print(0)
        return
    nums = [0] * (K + 1)
    nums[0] = 1
    for i in range(1, K + 1):
        for j in range(1, 10):
            if i - j < 0:
                break
            nums[i] += nums[i - j]
            nums[i] %= 10**9 + 7
    print(nums[K])


if __name__ == "__main__":
    # debug_input()
    main()
