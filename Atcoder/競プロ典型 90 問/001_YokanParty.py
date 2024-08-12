import io
import sys

_INPUT = """\
3 34
1
8 13 26

"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))

    def can_cut_yokan(min_size):
        cut_count = 0
        pre_cut_pos = 0
        for a in A:
            if a - pre_cut_pos < min_size:
                continue
            if L - a < min_size:
                break
            cut_count += 1
            pre_cut_pos = a
        return cut_count >= K

    left = 0
    right = L + 1
    while left <= right:
        mid = (left + right) // 2
        if left == mid:
            break
        if can_cut_yokan(mid):
            left = mid
        else:
            right = mid - 1
    print(left)


if __name__ == "__main__":
    debug_input()
    main()
