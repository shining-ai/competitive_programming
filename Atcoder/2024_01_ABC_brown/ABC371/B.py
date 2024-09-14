import io
import sys

_INPUT = """\
2 4
1 M
1 M
2 F
2 M
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M = map(int, input().split())
    done = set()
    for _ in range(M):
        home, sex = input().split()
        if home in done:
            print("No")
            continue
        if sex == "F":
            print("No")
            continue
        print("Yes")
        done.add(home)




if __name__ == "__main__":
    # debug_input()
    main()
