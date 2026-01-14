import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 0199 2026-01-13 Start time: 21:38 End time: 21:47
#######################################################################
problem = """
199. Binary Tree Right Side View
Medium

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:



Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""

#######################################################################
# Notes
#######################################################################

notes = """
Track the depth and the left-ness

OR

Use BFS (simpler)

MISTAKE: 
- Did not include the case where the root node is null
- Did not actually include a return statement

"""

#######################################################################
# Solution
#######################################################################

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        right_side_view: List[int] = []
        queue = [root]
        next_level = []
        while len(queue) > 0:
            node = queue.pop()
            if node.left:
                next_level.insert(0,node.left)
            if node.right:
                next_level.insert(0,node.right)
            
            if len(queue) == 0:
                right_side_view.append(node.val)
                queue = next_level
                next_level = []
        return right_side_view
            
            
            

