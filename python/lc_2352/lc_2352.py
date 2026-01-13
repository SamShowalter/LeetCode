import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 2352 2026-01-08 Start time: 10:36 End time: 10:47
#######################################################################
problem = """
2352. Equal Row and Column Pairs
Medium

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
"""

#######################################################################
# Notes
#######################################################################

notes = """
Ideally, we should only have to traverse the items as few times as possible

Got it first try, but the solution was slow for some reason
"""

#######################################################################
# Solution
#######################################################################

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        side_len = len(grid)

        numPairs = 0

        for r in range(side_len):
            for c in range(side_len):
                # Had order of this wrong
                i = 0
                while (i < side_len) and (grid[r][i] == grid[i][c]):
                    i += 1
                if i == side_len:
                    numPairs += 1

        return numPairs

s = Solution()
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(s.equalPairs(grid))
        
