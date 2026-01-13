import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 1448 2026-01-11 Start time: 19:38 End time: 19:42
#######################################################################
problem = """
1448. Count Good Nodes in Binary Tree
Medium

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
"""


#######################################################################
# Notes
#######################################################################

notes = """
Recursive again, but this time you tack the max value

MISTAKE: 
- I used zero as min value, should have been -inf
- Could also seed it with something else

"""

#######################################################################
# Solution
#######################################################################

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def _goodNodes(self, root: TreeNode, maxVal: int) -> int:
        if root is None:
            return 0
        else:
            goodNode: int = 1 if maxVal <= root.val else 0
            return (goodNode + 
                self._goodNodes(root.left, max(maxVal,root.val)) +
                self._goodNodes(root.right, max(maxVal,root.val))
            )
        
    def goodNodes(self, root: TreeNode) -> int:
        return self._goodNodes(root,-int("inf"))
        
