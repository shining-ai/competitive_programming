import io
import sys

_INPUT = """\
3 4
1 1
2 5
7 4
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


# 身長・体重を表にまとめ、累積和を取る
def main():
    MAX_HEIGHT = 5000
    MAX_WEIGHT = 5000
    MAX_K = 5000

    N, K = map(int, input().split())
    menber_table = [[0] * (MAX_HEIGHT + 1) for _ in range(MAX_WEIGHT + 1)]
    for _ in range(N):
        a, b = map(int, input().split())
        menber_table[a][b] += 1
    for i in range(1, MAX_HEIGHT + 1):
        for j in range(1, MAX_WEIGHT + 1):
            menber_table[i][j] += menber_table[i][j - 1]
    for j in range(1, MAX_WEIGHT + 1):
        for i in range(1, MAX_HEIGHT + 1):
            menber_table[i][j] += menber_table[i - 1][j]

    max_team = 0
    for min_height in range(1, MAX_HEIGHT + 1):
        for min_weight in range(1, MAX_WEIGHT + 1):
            border_height = min_height + K
            if border_height > MAX_HEIGHT:
                break
            border_weight = min_weight + K
            if border_weight > MAX_WEIGHT:
                break
            team = (
                menber_table[border_height][border_weight]
                - menber_table[border_height][min_weight - 1]
                - menber_table[min_height - 1][border_weight]
                + menber_table[min_height - 1][min_weight - 1]
            )
            max_team = max(max_team, team)
    print(max_team)


if __name__ == "__main__":
    # debug_input()
    main()
