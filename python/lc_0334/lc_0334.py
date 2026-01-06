import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 0334
#######################################################################
problem = """
334. Increasing Triplet Subsequence
Medium

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""

#######################################################################
# Notes
#######################################################################

notes = """
Technically just running out the pointers in O(n) time
- when arr[i] >= arr[j], move everything forward
- when arr[j] >= arr[k], just move j and k forward

VERY CHALLENGING
- Less than or equal to is essential to ensure things are not equal
- Second smallest must be > smallest
- The order or assignment also really matters

Took 3 Submission tries and a lot of thinking
"""

#######################################################################
# Solution
#######################################################################

class Solution:
    def increasingTriplet(self, arr: List[int]) -> bool:
        arrlen = len(arr)
        if arrlen < 3: return False
        
        smallest = float("inf")
        second_smallest = float("inf")
        # [2,1,5,0,4,6]

        for i in range(arrlen):
            if arr[i] <= smallest:
                smallest = arr[i]
            elif arr[i] <= second_smallest:
                second_smallest = arr[i]
            elif second_smallest > smallest:
                return True

        return False
                
            

s = Solution()
arr = [1,1,1,1,1]
"""
20,100
20,100



"""
print(s.increasingTriplet(arr))
