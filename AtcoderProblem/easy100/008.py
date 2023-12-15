import io
import sys


def debug_input():
    _INPUT = """\
100 100
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    A, B = map(int, input().split())

    data_str = str(A) + str(B)
    data = int(data_str)

    data_sqrt = data ** 0.5
    if data_sqrt.is_integer():
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    # debug_input()
    main()
