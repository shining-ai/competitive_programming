import io
import sys


def debug_input():
    _INPUT = """\
5 100 200

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    K, G, M = map(int, input().split())
    grass = 0
    magcup = 0

    for i in range(K):
        if grass == G:
            grass = 0
        elif magcup == 0:
            magcup = M
        else:
            if magcup >= G - grass:
                magcup -= G - grass
                grass = G
            else:
                grass += magcup
                magcup = 0

    print(grass, magcup)



if __name__ == "__main__":
    # debug_input()
    main()
