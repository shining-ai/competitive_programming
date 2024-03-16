import collections
import io
import sys


def debug_input():
    _INPUT = """\
aaaaa

    """



    sys.stdin = io.StringIO(_INPUT)


def main():
    S = input()

    hash_map = collections.defaultdict(int)
    for c in S:
        hash_map[c] += 1

    ans = 0
    for k, v in hash_map.items():
        if v >= 2:
            ans = 1

    S_num = len(S)
    for c in S:
        ans += S_num - hash_map[c]
        hash_map[c] -= 1
        S_num -= 1

    print(ans)



if __name__ == "__main__":
    # debug_input()
    main()
