import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 0283
#######################################################################
problem = """
283. Move Zeroes
Easy

Hint
Given an integer array arr, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
"""

#######################################################################
# Notes
#######################################################################

notes = """
Swap values?
- If we run into another zero, then we should swap that too
- Could start from RHS

[1,1,0,0]

NOTES: Correct first try, but the way I swap items is sub-optimal because I am bubbling 
things up. Could do better to go left to right and swap the first non-zero elements.

"""

#######################################################################
# Solution
#######################################################################

class Solution:
    def swap(self,arr, i, j) -> None:
        arr[i], arr[j] = arr[j], arr[i]
        
    def moveZeroes(self, arr: List[int]) -> List[int]:
        """
        Do not return anything, modify arr in-place instead.
        """
        arrlen = len(arr)
        i = arrlen-1
        curr_end = i

        while i >= 0:
            if (arr[i] == 0):
                while (i < curr_end) and (arr[i+1] != 0):
                    self.swap(arr, i, i+1)
                    i += 1
                curr_end -= 1
                i = curr_end-1
            else:
                i -= 1
        return arr

                
a = [0,1]
s = Solution()
print(s.moveZeroes(a))
