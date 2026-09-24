# https://leetcode.com/problems/number-of-distinct-islands/description/

# ## Example 1: Basic Distinct Shapes## Input Grid

# [,
#  ,
#  ,
#   [0, 0, 0, 1, 1]
# ]

# ## Output

# 1

# ## Description

# * There are two islands in this grid.
# * The first island is in the top-left corner, and the second island is in the bottom-right corner.
# * Both islands form an identical 2x2 square block. Because they have the exact same shape and orientation, they are not counted separately.
# * Therefore, there is only 1 distinct island shape.

# ------------------------------
# ## Example 2: Same Blocks, Different Orientations## Input Grid

# [,
#  ,
#  ,
#  ,
#   [0, 1, 0, 1, 0]
# ]

# ## Output

# 3

# ## Description
# There are four total islands in this grid, but only 3 unique shapes:

#    1. Top-Left Island: Shaped like a backward "L" ([[1,1], [1,0]]).
#    2. Top-Right Island: Shaped like an "L" ([[1,1], [0,1]]). Even though it has the same number of blocks as the top-left island, rotations do not count as the same shape. This is unique.
#    3. Bottom-Left Island: Shaped like an "L" ([[1,1], [0,1]]). This matches the top-right island perfectly by sliding (translation). It is a duplicate.
#    4. Bottom-Right Island: Shaped like an inverted "T" or a corner ([[1,1], [1,0]] shifted). It is a unique shape.

# ------------------------------
# ## Example 3: Single Cells and Complex Paths## Input Grid

# [,
#  ,
#   [1, 0, 1]
# ]

# ## Output

# 1

# ## Description

# * There are four separate islands, each consisting of exactly one single cell (1) at the corners.
# * Since a single cell translated anywhere else is still just a single cell, all four share the exact same shape.
# * The number of distinct island shapes is 1.

# Would you like to see how the DFS path tracking looks for these shapes, or should we write the Python code to process these exact inputs?

