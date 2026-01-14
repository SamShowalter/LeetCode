import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 2336 2026-01-12 Start time: 19:10 End time: 19:17
#######################################################################
problem = """
236. Lowest Common Ancestor of a Binary Tree
Medium

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""

#######################################################################
# Notes
#######################################################################

notes = """
You have definitely seen this one before when the tree is sorted
- The tree is no longer sorted though

First try! But did take a few hints from the book
- I was also thinking about tracking with a list but it ended up not being necessary

"""

#######################################################################
# Solution
#######################################################################

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

class Solution:
    def _lowestCommonAncestor(self,root,p,q) -> Optional[TreeNode]:
        
        if root is None:
            return None
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root
        
        else:
            return left if left is not None else right
        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self._lowestCommonAncestor(root,p,q)
        
        
