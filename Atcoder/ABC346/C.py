import io
import sys


def debug_input():
    _INPUT = """\
10 158260522
877914575 24979445 623690081 262703497 24979445 1822804784 1430302156 1161735902 923078537 1189330739

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    seen = set()
    for a in A:
        if a in seen:
            continue
        if 1 <= a <= K:
            ans -= a
            seen.add(a)

    ans += K * (K + 1) // 2
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
