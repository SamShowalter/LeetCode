import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 1493 2026-01-07 Start time: 3:52 End time: 3:54
#######################################################################
problem = """
1493. Longest Subarray of 1's After Deleting One Element
Medium

Hint
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

#######################################################################
# Notes
#######################################################################

notes = """
This feels like a trivial extension of the other problem. Just imagine your budge is 1, then delete one at end

"""

#######################################################################
# Solution
#######################################################################

class Solution:
    
    def longestOnes(self, arr: List[int], k: int) -> int:
        i = 0; j=0

        nums_len = len(arr)
        spots_used: int = 0
        longestOnes: int = 0

        while (j < nums_len):
            if arr[j] == 0:
                if spots_used < k:
                    spots_used += 1
                    j += 1
                else:
                    if arr[i] == 0:
                        spots_used -= 1
                    i += 1
            else:
                j += 1

            # MISTAKE: j - i is correct, not j-i + 1
            longestOnes = max(longestOnes, j-i)
            
        return longestOnes
    
    def longestSubarray(self, arr: List[int]) -> int:
        return self.longestOnes(arr,1) - 1

s = Solution()
arr = [1,1,0,1]
print(s.longestSubarray(arr))
