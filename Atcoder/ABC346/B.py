import io
import sys


def debug_input():
    _INPUT = """\
92 66


    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    W, B = map(int, input().split())
    piano = "wbwbwwbwbwbw" *20

    n = 240 // (W + B) + 1
    for i in range(240 - (W + B) + 1):
        count_w = 0
        count_b = 0
        for p in piano[i:i + W + B]:
            if p == "w":
                count_w += 1
            else:
                count_b += 1
        if count_w == W and count_b == B:
            print("Yes")
            break
    else:
        print("No")

if __name__ == "__main__":
    # debug_input()
    main()
