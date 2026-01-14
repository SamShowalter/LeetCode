import os
import sys
from typing import Dict, List, Optional

#######################################################################
# Problem # 1372 2026-01-12 Start time: 19:00 End time: 19:09
#######################################################################
problem = """
1372. Longest ZigZag Path in a Binary Tree
Medium

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

 

Example 1:


Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
Example 2:


Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
Example 3:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 5 * 104].
1 <= Node.val <= 100
"""

#######################################################################
# Notes
#######################################################################

notes = """
<<<<<<< Updated upstream
The longest path must start at root?
- No it doesn't

Track the max through a class variable?

Running into an issue with 

=======
GOT IT!! Main mistake was not adding the minus 1
>>>>>>> Stashed changes
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

    def _longestZigZag(self, root, last_dir: str, currSum: int) -> unt:
        self.maxZigZag = max(self.maxZigZag, currSum)
        if root is None:
            return
        elif last_dir == "left":
            self._longestZigZag(root.left, "left", 1)
            self._longestZigZag(root.right, "right", currSum+1)
        elif last_dir == "right":
            self._longestZigZag(root.right, "right", 1)
            self._longestZigZag(root.left, "left", currSum+1)
            
            
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxZigZag = 0
        self._longestZigZag(root, "left", 0)
        self._longestZigZag(root, "right", 0)
        # Mistake: needed a -1 here
        return self.maxZigZag - 1
