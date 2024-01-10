import collections


def solve_1(s):
    counts = collections.Counter(s)

    for i, i_s in enumerate(s):
        if counts[i_s] == 1:
            return i

    return -1


if __name__ == "__main__":
    s = "loveleetcode"
    print(solve_1(s))
