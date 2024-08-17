import io
import sys

sys.setrecursionlimit(10000)
_INPUT = """\
3 2
2 1 3
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())
    R = list(map(int, input().split()))
    all_num = []

    def all_loop(r_i, curr):
        if r_i == len(R):
            if sum(curr) % K == 0:
                all_num.append(curr[:])
            return
        for i in range(1, R[r_i] + 1):
            curr.append(i)
            all_loop(r_i + 1, curr)
            curr.pop()
        return

    all_loop(0, [])
    for num in all_num:
        print(" ".join(map(str, num)))


if __name__ == "__main__":
    # debug_input()
    main()
