import io
import sys


def debug_input():
    _INPUT = """\
6
3 2
1 6
4 5
1 3
5 5
9 8

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]

    def calc_distance(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    for point in points:
        max_distance = 0
        ans_index = 0
        for i, target_point in enumerate(points):
            distance = calc_distance(point, target_point)
            if distance > max_distance:
                max_distance = distance
                ans_index = i
        print(ans_index + 1)


if __name__ == "__main__":
    # debug_input()
    main()
