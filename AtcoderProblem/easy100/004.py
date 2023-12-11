import io
import sys


def debug_input():
    _INPUT = """\
    1001
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N!)
def main():
    N = int(input())

    price = N / 1.08
    item = int(price)

    if int(item * 1.08) == N:
        print(item)
    elif int((item + 1) * 1.08) == N:
        print(item + 1)
    else:
        print(":(")


if __name__ == "__main__":
    # debug_input()
    main()
