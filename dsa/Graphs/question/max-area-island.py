# https://leetcode.com/problems/max-area-of-island/description/

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]





class Solution:
    def dfs(self, i: int, j: int, grid: list[list[int]]) -> int:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                    return 0

        # Mark cell as visited
        grid[i][j] = 0

        # 1 (current cell) + areas from all 4 directions
        return (
            1
            + self.dfs(i - 1, j, grid)
            + self.dfs(i + 1, j, grid)
            + self.dfs(i, j - 1, grid)
            + self.dfs(i, j + 1, grid)
        )
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(i, j, grid))

        return max_area
        


             




print(numOfIsland(grid))