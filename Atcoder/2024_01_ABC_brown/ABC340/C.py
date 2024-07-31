import io
import math
import sys
from collections import defaultdict


def debug_input():
    _INPUT = """\
        10
    """

    sys.stdin = io.StringIO(_INPUT)


# def main(N):
#     # N = int(input())
#     dp = defaultdict(int)
#     dp[1] = 0
#     dp[2] = 2
#     dp[3] = 5
#     ans = 0

#     def point(n):
#         if n in dp:
#             return dp[n]
#         else:
#             dp[n] = point(n // 2) + point(math.ceil(n / 2)) + n
#             return dp[n]

#     # print(point(N))
#     return point(N)


# def test(N):
#     # N = int(input())
#     ans = 0
#     queue = [N]
#     while queue:
#         n = queue.pop()
#         if n <= 1:
#             continue
#         ans += n
#         queue.append(n // 2)
#         queue.append(math.ceil(n / 2))

#     # print(ans)
#     return ans


# # 3 2+3
# # 4 2+3+3
# # 5 2+3+3+4
def main():
    N = int(input())
    repeat = 1
    val = 2
    ans = 0
    while N > repeat:
        N -= repeat
        ans += val * repeat
        val += 1
        repeat = repeat * 2

    ans += (N - 1) * val
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()

    # for i in range(1, 30):
    #     #     if test(i) != main(i):
    #     #         print(i)
    #     # print("end")
    #     res = test(i)
    #     # print(f"{format(i-1, '08b')} : {i}: {res - test(i - 1)} : {res}")
    #     res2 = test2(i)
    #     print(f"{i}: {res} : {res2}")
