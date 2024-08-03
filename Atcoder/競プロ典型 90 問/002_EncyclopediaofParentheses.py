import io
import sys

_INPUT = """\
4
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    if N % 2 == 1:
        return
    bit_patterns = []

    def correct_bracket(bit_pattern):
        needed_close_num = 0
        for bit in bit_pattern:
            if bit == "0":
                needed_close_num += 1
                continue
            needed_close_num -= 1
            if needed_close_num < 0:
                return False
        return needed_close_num == 0

    for i in range(1 << N):
        bit_pattern = bin(i)[2:].zfill(N)
        if not correct_bracket(bit_pattern):
            continue
        print(bit_pattern.replace("0", "(").replace("1", ")"))


if __name__ == "__main__":
    # debug_input()
    main()
