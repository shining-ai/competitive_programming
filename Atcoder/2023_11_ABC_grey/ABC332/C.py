import io
import sys


def debug_input():
    _INPUT = """\
3 1
222

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M = map(int, input().split())
    S = input()

    plain_t = M
    logo_t = 0

    ans = 0

    for i_s in S:
        if i_s == "0":
            plain_t = M
            logo_t = ans
        elif i_s == "1":
            if plain_t >= 1:
                plain_t -= 1
            else:
                if logo_t >= 1:
                    logo_t -= 1
                else:
                    ans += 1
        else:
            if logo_t >= 1:
                logo_t -= 1
            else:
                ans += 1

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
