import io
import sys

_INPUT = """\
2
1 2
1 2

"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(list(map(int, input().split())) for _ in range(N))

    def count_inversion(left_range, right_range):
        right_min = right_range[0]
        right_max = right_range[1]
        left_min = left_range[0]
        left_max = left_range[1]
        pattern = 0
        for left in range(left_max, left_min - 1, -1):
            if left <= right_min:
                break
            if left <= right_max:
                pattern += left - right_min
            else:
                pattern += right_max - right_min + 1
        return pattern

    expected_value = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            pattern = count_inversion(A[i], A[j])
            all_pattern = (A[i][1] - A[i][0] + 1) * (A[j][1] - A[j][0] + 1)
            expected_value += pattern / all_pattern
    print(expected_value)


if __name__ == "__main__":
    # debug_input()
    main()
