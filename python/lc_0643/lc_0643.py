import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 0643 Start time: 3:21 End time: 3:41
#######################################################################
problem = """
643. Maximum Average Subarray I
Easy

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""

#######################################################################
# Notes
#######################################################################

notes = """
Just drag the average around and determine with slicing

MISTAKE:
- Errors around index at zero, up to but not including slicing, etc. common
- Should review and be careful around these things

ERROR: TIME LIMIT RAN OUT
- I need a better complexity by not computing averages until the end
- This one is dumb - doubt people will test this
"""

#######################################################################
# Solution
#######################################################################

class Solution:
        
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = k-1
        nums_len = len(nums)
        max_sum = sum(arr[:k])
        curr_sum = max_sum

        for i in range(k, nums_len):
            # Need minus 1 because of zero indexing
            # Can skip if we see it won't matter
            curr_sum -= arr[i-k]
            curr_sum += arr[i]
            max_sum = max(max_sum, curr_sum)
                
        return max_sum/k

s = Solution()
arr= [0,1,1,3,3]
print(s.findMaxAverage(arr,4))
        
        

