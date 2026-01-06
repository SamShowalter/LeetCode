import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 0011 Start: 3:09, Finish 3:15
#######################################################################
problem = """

11. Container With Most Water
Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

#######################################################################
# Notes
#######################################################################

notes = """
Maintain a running max height seen so far
- Except the distance to produce the area is also needed
- Maybe we need to be computing the max area possible thus far?

Plan:
- Set the pointers as far away as possible to start. 
- Move the pointer with the lower line. Track the current maximum

TOOK A BIG HINT TO START POINTERS AS FAR AWAY AS POSSIBLE AND MOVE SHORTER ONE

"""

#######################################################################
# Solution
#######################################################################

class Solution:
    def getArea(self,height, x1, x2) -> int:
        return height * (x2-x1)
        
    def maxArea(self, arr: List[int]) -> int:
        i = 0
        j = len(arr)-1
        curr_max_area = 0

        while (i < j):
            min_height = min(arr[i],arr[j])
            curr_max_area = max(self.getArea(
                min_height, i, j 
            ), curr_max_area)

            if (min_height == arr[i]):
                i += 1
            else: 
                j -=1
                
        return curr_max_area

            
s = Solution()
arr = [1,8,6,2,5,4,8,3,7]
print(s.maxArea(arr))
            
        
        
