import copy


# O(n^2) time
# O(n) space
def solve_1(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    money_dp = [[False] * (n * 400) for _ in range(n + 1)]
    money_dp[0][0] = True
    money_dp[1][0] = True
    money_dp[1][nums[0]] = True

    for i, i_money in enumerate(nums[1:], start=2):
        money_dp[i] = copy.deepcopy(money_dp[i - 1])
        for j in range(n * 400):
            if money_dp[i - 2][j]:
                money_dp[i][j + i_money] = True

    for i in range(n * 400 - 1, -1, -1):
        if money_dp[-1][i]:
            return i


if __name__ == "__main__":
    nums = [1, 3, 1, 3, 100]
    print(solve_1(nums))
