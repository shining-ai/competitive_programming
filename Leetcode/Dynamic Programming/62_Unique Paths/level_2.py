class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        route_num = factorial(n + m - 2) // (
            factorial(m - 1) * factorial(n - 1)
        )
        return route_num
