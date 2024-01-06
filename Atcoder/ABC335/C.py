import io
import sys


def debug_input():
    _INPUT = """\
5 9
2 3
1 U
2 3
1 R
1 D
2 3
1 L
2 1
2 5
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, Q = map(int, input().split())
    move_pos = [[1, 0]]

    querys = [list(map(str, input().split())) for _ in range(Q)]
    curr = [1, 0]
    q1_num = 0
    for q, p in querys:
        if q == "1":
            if p == "U":
                curr[1] += 1
            elif p == "D":
                curr[1] -= 1
            elif p == "R":
                curr[0] += 1
            elif p == "L":
                curr[0] -= 1
            move_pos.append(list(curr))
            q1_num += 1
        else:
            if int(p) > q1_num:
                print(int(p) - q1_num, 0)
            else:
                ans = move_pos[abs(int(p) - q1_num) + 1]
                print(ans[0], ans[1])


if __name__ == "__main__":
    # debug_input()
    main()
