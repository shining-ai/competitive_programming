import io
import sys
from collections import defaultdict

_INPUT = """\
8
1 3
1 1
1 4
3
2 1
3
1 5
3
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    Q = int(input())
    bag = defaultdict(int)
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            bag[int(query[1])] += 1
        elif query[0] == "2":
            bag[int(query[1])] -= 1
            if bag[int(query[1])] == 0:
                bag.pop(int(query[1]))
        else:
            print(len(bag))


if __name__ == "__main__":
    # debug_input()
    main()
