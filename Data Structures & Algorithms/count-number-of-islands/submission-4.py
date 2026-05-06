class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        count = 0

        def dfs(row, col):
            if row < 0 or row >= r or col < 0 or col >= c:
                return 
            if grid[row][col] == "0":
                return 
            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row - 1, col)
            dfs(row, col - 1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count        