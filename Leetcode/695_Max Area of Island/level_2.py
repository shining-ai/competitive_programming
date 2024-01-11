# O(m*n) time complexity
# O(m*n) space complexity
def main(grid):
    row_num = len(grid)
    collumn_num = len(grid[0])
    ans = 0

    def dfs(grid, row, collumn):
        island_size = 0

        if row < 0 or collumn < 0 or row >= row_num or collumn >= collumn_num:
            return 0

        if grid[row][collumn] == 0:
            return 0

        grid[row][collumn] = 0
        island_size += dfs(grid, row - 1, collumn)
        island_size += dfs(grid, row + 1, collumn)
        island_size += dfs(grid, row, collumn - 1)
        island_size += dfs(grid, row, collumn + 1)
        return island_size + 1

    for i in range(row_num):
        for j in range(collumn_num):
            if grid[i][j] == 1:
                island_size = dfs(grid, i, j)
                ans = max(ans, island_size)

    return ans


if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    print(main(grid))
