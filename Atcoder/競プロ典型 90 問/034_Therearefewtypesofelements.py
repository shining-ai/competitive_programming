import io
import sys
from collections import defaultdict

_INPUT = """\
5 1
1 2 3 4 5
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    subarray_num = defaultdict(int)
    max_length = 0
    left = 0
    for right in range(N):
        subarray_num[a[right]] += 1
        while K < len(subarray_num):
            subarray_num[a[left]] -= 1
            if subarray_num[a[left]] == 0:
                del subarray_num[a[left]]
            left += 1
        max_length = max(max_length, right - left + 1)

    print(max_length)


if __name__ == "__main__":
    # debug_input()
    main()
