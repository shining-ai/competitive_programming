import io
import sys


def debug_input():
    _INPUT = """\
10 2 3
abccabaabb

    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N!)
def main():
    N, A, B = map(int, input().split())
    S = input()

    pass_count = 0
    foreign_count = 0
    for i_rank, i_s in enumerate(S):
        if pass_count >= A + B:
            print("No")
        else:
            if i_s == "a":
                if pass_count <= A + B:
                    pass_count += 1
                    print("Yes")
                else:
                    print("No")
            elif i_s == "b":
                foreign_count += 1
                if pass_count <= A + B and foreign_count <= B:
                    pass_count += 1
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")


if __name__ == "__main__":
    # debug_input()
    main()
