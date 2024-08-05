import io
import sys

_INPUT = """\
1024
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    prime_num = 1
    i = 2
    while i <= N**0.5:
        if N % i == 0:
            N = N // i
            prime_num += 1
        else:
            i += 1
    magic_count = 0
    while 2**magic_count < prime_num:
        magic_count += 1
    print(magic_count)


if __name__ == "__main__":
    # debug_input()
    main()
