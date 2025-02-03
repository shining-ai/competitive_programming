import io
import sys
import bisect


def debug_input():
    _INPUT = """\
6
insert AAA
insert AAC
find AAA
find CCC
insert CCC
find CCC
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    n = int(input())
    dic = {}
    for _ in range(n):
        command, key = input().split()
        if command == "insert":
            dic[key] = True
            continue
        if key in dic:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    # debug_input()
    main()
