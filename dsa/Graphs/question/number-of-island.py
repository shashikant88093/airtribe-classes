# https://leetcode.com/problems/number-of-islands/description/



grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]


def dfs(i,j,grid):
    if (i<0 or i>=len(grid) or (j<0) or j>=len(grid[0]) or grid[i][j]== 0):
        return
    grid[i][j] = 0

    dfs(i+1,j,grid)
    dfs(i-1,j,grid)
    dfs(i,j-1,grid)
    dfs(i,j+1,grid)

def numOfIsland(grid):
    noi =0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                noi+=1
                dfs(i,j,grid)
    return noi
