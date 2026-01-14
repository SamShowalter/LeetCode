import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 0700 2026-01-13 Start time: 22:00 End time: 
#######################################################################
problem = """
700. Search in a Binary Search Tree
Easy

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
"""

#######################################################################
# Notes
#######################################################################

notes = """
Simple BST, can use recursion
- Flipped the sign of the conditions at first, silly error
"""

#######################################################################
# Solution
#######################################################################

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val == val:
            return root
        # Silly mistake, flipped the sign
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
            
