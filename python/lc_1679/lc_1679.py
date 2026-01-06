import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 1679 Started 3:16, Finished 3:20
#######################################################################
problem = """
1679. Max Number of K-Sum Pairs
Medium

Hint

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""

#######################################################################
# Notes
#######################################################################

notes = """
Sort the array first. Then walk the pointers down based on too big or too small
- If you do an operation, you need to increment both pointers

"""

#######################################################################
# Solution
#######################################################################

class Solution:
    def maxOperations(self, arr: List[int], k: int) -> int:
        arr = list(sorted(arr))
        arr_len = len(arr)

        i = 0
        j = arr_len - 1 # MISTAKE: put off the end of list (no - 1)
        maxOps = 0

        while (i < j):
            if arr[i] + arr[j] > k:
                j -=1
            elif (arr[i] + arr[j] < k):
                i += 1
            else:
                maxOps += 1
                i += 1
                j -= 1
                
        return maxOps

s = Solution()
arr = [3,1,3,4,3]
print(s.maxOperations(arr, 5))


        

