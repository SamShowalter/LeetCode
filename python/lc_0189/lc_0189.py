
import os
import sys
from typing import Dict, List

#######################################################################
# Problem
#######################################################################
problem = """
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

#######################################################################
# Notes
#######################################################################

notes = """

"""
 

#######################################################################
# Solution
#######################################################################

class Solution:
    def rotateArrayNewArr(self,nums:List[int], rotated: int):
        l = len(nums)
        new_arr = [
            nums[(i-rotated)%l] 
            for i in range(l)
        ]
        return new_arr

    def rotateArray(self, nums: List[int], rotated: int):
        l = len(nums)
        hold = nums[0]
        shift = (rotated)%l
        start = True
        while shift != 0 or start:
            start = False
            nums[shift], hold = hold, nums[shift]
            shift = (shift+rotated)%l

        # Need exit condition, one last time
        nums[shift], hold = hold, nums[shift]
        
        return nums
            


sol = Solution()

arr =[1,2,3,4] 
"""
[1,2,3,4]
[3,2,1,4]
[3,2,1,4]
"""
print(sol.rotateArray(arr,2))

    
 
