import collections
import io
import sys


def debug_input():
    _INPUT = """\
atcoder


    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    S = input()
    count_s = collections.defaultdict(int)

    for i_s in S:
        count_s[i_s] += 1

    ans = ""
    ans_num = 0

    count_s = sorted(count_s.items(), key=lambda x: x[0])

    for i in count_s:
        char, num = i
        if ans_num < num:
            ans = char
            ans_num = num

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
