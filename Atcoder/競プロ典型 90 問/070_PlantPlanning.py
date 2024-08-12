import io
import sys

_INPUT = """\
2
-1 2
1 1
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


# 中央値が答えになる
def main():
    N = int(input())
    X, Y = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()
    x_middle = X[N // 2]
    y_middle = Y[N // 2]

    distance = 0
    for x, y in zip(X, Y):
        distance += abs(x - x_middle) + abs(y - y_middle)
    print(distance)


if __name__ == "__main__":
    # debug_input()
    main()
