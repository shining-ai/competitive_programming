import io
import sys
import bisect


def debug_input():
    _INPUT = """\
5 3
8
1
7
3
9
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    n, k = map(int, input().split())
    weights = [int(input()) for _ in range(n)]

    def can_ship(max_load):
        current = 0
        needed_truck = 1
        for weight in weights:
            current += weight
            if current <= max_load:
                continue
            needed_truck += 1
            current = weight
            if needed_truck > k:
                return False
        return needed_truck <= k

    left = max(weights)
    right = sum(weights)
    while left < right:
        mid = (left + right) // 2
        if can_ship(mid):
            right = mid
        else:
            left = mid + 1
    print(left)


if __name__ == "__main__":
    # debug_input()
    main()
