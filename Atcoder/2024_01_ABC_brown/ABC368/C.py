import io
import sys

_INPUT = """\
2
2 5
"""
# T = 0

# 1 → 1  1 // 5 = 0
# 2 → 2  2 // 5 = 0
# 3 → 3  3 // 5 = 0
# 4 → 3  4 // 5 = 0
# 5 → 3  5 // 5 = 1

# 6 → 4
# 7 → 5
# 8 → 6
# 9 → 6
# 10 → 6


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    H = list(map(int, input().split()))
    T = 0

    for h in H:
        while T % 3 != 2:
            h -= 1
            T += 1
            if h <= 0:
                break
        if h <= 0:
            continue
        loop = h // 5
        T += loop * 3
        remain = h % 5
        if remain == 4:
            T += 2
        elif remain == 0:
            pass
        else:
            T += 1
    print(T)


if __name__ == "__main__":
    # debug_input()
    main()
