import io
import sys


def debug_input():
    _INPUT = """\
10
690830957 868532399
741145463 930111470
612846445 948344128
540375785 925723427
723092548 925021315
928915367 973970164
563314352 832796216
562681294 868338948
923012648 954764623
691107436 891127278
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    man = []
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        man.append((B - A, A, B))

    man = sorted(man, reverse=True)
    total = man[0][2]
    for i in range(1, N):
        total += man[i][1]
    print(total)


if __name__ == "__main__":
    # debug_input()
    main()
