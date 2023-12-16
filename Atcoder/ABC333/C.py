import io
import sys


def debug_input():
    _INPUT = """\
    333


    """

    sys.stdin = io.StringIO(_INPUT)


def calc_repunit(i):
    base = "1"
    return int(base * i)


def main():
    N = int(input())
    ans = 0
    cnt = 0

    for i in range(1, N + 1):
        for j in range(1, i + 1):
            for k in range(1, j + 1):
                cnt += 1
                if cnt == N:
                    ans = calc_repunit(i) + calc_repunit(j) + calc_repunit(k)
                    break
            if ans != 0:
                break
        if ans != 0:
            break

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
