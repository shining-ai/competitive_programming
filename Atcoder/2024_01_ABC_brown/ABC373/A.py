import io
import sys

_INPUT = """\
january
february
march
april
may
june
july
august
september
october
november
december
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    count = 0
    for i in range(1, 13):
        if i == len(input()):
            count += 1
    print(count)


if __name__ == "__main__":
    # debug_input()
    main()
