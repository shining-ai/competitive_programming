import io
import math
import sys


def debug_input():
    _INPUT = """\
2 2 3
1 5

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, A, B = map(int, input().split())
    D = list(map(int, input().split()))
    week = A + B
    days = set()
    # 2週間分のデータを作成するとつなぎを考慮しなくてもよい
    for d in D:
        d_week = d % week
        days.add(d_week)
        days.add(d_week + week)

    days = list(days)
    days.sort()
    # 休日に収まっている => 平日に予定がない
    # B日連続で予定がなければYES
    # 前の予定から次の予定までにB日間空いている部分があればいい
    for i in range(len(days) - 1):
        if (days[i + 1] - days[i]) > B:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    # debug_input()
    main()
