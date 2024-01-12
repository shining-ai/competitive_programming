# O(M * N) time complexity
# O(M * N) space complexity
def main(grid):
    row_num = len(grid)
    collumn_num = len(grid[0])

    def dfs(grid, row, collumn):
        if row < 0 or collumn < 0 or row >= row_num or collumn >= collumn_num:
            return

        if grid[row][collumn] == "0":
            return

        grid[row][collumn] = "0"
        dfs(grid, row - 1, collumn)
        dfs(grid, row + 1, collumn)
        dfs(grid, row, collumn - 1)
        dfs(grid, row, collumn + 1)

    ans = 0

    for i in range(row_num):
        for j in range(collumn_num):
            if grid[i][j] == "1":
                dfs(grid, i, j)
                ans += 1

    return ans


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    print(main(grid))
