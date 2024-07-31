import collections
import io
import sys


def debug_input():
    _INPUT = """\
ab
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    S = input()
    count_char = collections.Counter(S)
    nums = list(count_char.values())
    count_nums = collections.Counter(nums)
    ans = "Yes"
    for i in count_nums.values():
        if i != 2:
            ans = "No"
            break
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
