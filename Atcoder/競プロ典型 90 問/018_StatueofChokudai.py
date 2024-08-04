import io
import sys
import math

_INPUT = """\
4
2 1 1
4
0
1
2
3
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    T = int(input())
    L, X, Y = map(int, input().split())
    statue_postion = (X, Y, 0)
    Q = int(input())
    for _ in range(Q):
        E = int(input())
        angle_of_wheel = ((-E / T - 0.25) % 1) * (math.pi * 2)  # 時計回り
        postion = (
            0,
            (L / 2) * math.cos(angle_of_wheel),
            (L / 2) * (1 + math.sin(angle_of_wheel)),
        )
        dist_3d = math.sqrt(
            (statue_postion[0] - postion[0]) ** 2
            + (statue_postion[1] - postion[1]) ** 2
            + (statue_postion[2] - postion[2]) ** 2
        )
        dist_2d = math.sqrt(
            (statue_postion[0] - postion[0]) ** 2
            + (statue_postion[1] - postion[1]) ** 2
        )
        print(math.degrees(math.acos(dist_2d / dist_3d)))


if __name__ == "__main__":
    # debug_input()
    main()
