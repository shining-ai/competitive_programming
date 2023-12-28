import io
import sys


def debug_input():
    _INPUT = """\
    3
    1 2 3
    2 3 4
    3 4 5
    """
    sys.stdin = io.StringIO(_INPUT)


def calc_plus_score(field, P, Q, R):
    field[P - 1] += 1
    field[Q - 1] += 1
    field[R - 1] += 1

    return field.count(0)


def calc_minus_score(field, P, Q, R):
    field[P - 1] -= 1
    field[Q - 1] -= 1
    field[R - 1] -= 1

    return field.count(0)


def calc_score(field, P, Q, R):
    plus_score = calc_plus_score(field, P, Q, R)
    minux_score = calc_minus_score(field, P, Q, R)

    return plus_score, minux_score


# ビームサーチ
def main():
    T = int(input())
    P = [None] * T
    Q = [None] * T
    R = [None] * T
    for i in range(T):
        P[i], Q[i], R[i] = map(int, input().split())
        P[i] -= 1  # 0 始まりに直す
        Q[i] -= 1
        R[i] -= 1
    # 配列 A の初期化

    A = [0] * 20

    # 貪欲法
    CurrentScore = 0
    for i in range(T):
        # パターン A の場合のスコアを求める
        ScoreA = CurrentScore
        PatA = [0] * 20
        for j in range(20):
            PatA[j] = A[j]
        PatA[P[i]] += 1
        PatA[Q[i]] += 1
        PatA[R[i]] += 1
        for j in range(20):
            if PatA[j] == 0:
                ScoreA += 1

        # パターン B の場合のスコアを求める
        ScoreB = CurrentScore
        PatB = [0] * 20
        for j in range(20):
            PatB[j] = A[j]
        PatB[P[i]] -= 1
        PatB[Q[i]] -= 1
        PatB[R[i]] -= 1
        for j in range(20):
            if PatB[j] == 0:
                ScoreB += 1

        # スコアの大きい方を採用
        if ScoreA >= ScoreB:
            print("A")
            CurrentScore = ScoreA
            for j in range(20):
                A[j] = PatA[j]
        else:
            print("B")
            CurrentScore = ScoreB
            for j in range(20):
                A[j] = PatB[j]


if __name__ == "__main__":
    # debug_input()
    main()
