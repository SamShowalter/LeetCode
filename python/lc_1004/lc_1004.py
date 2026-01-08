import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 1004 Start time: 3:44 End time: 3:51 (2026-01-07)
#######################################################################
problem = """
1004. Max Consecutive Ones III
Medium

Hint
Given a binary array arr and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: arr = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: arr = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= arr.length <= 105
arr[i] is either 0 or 1.
0 <= k <= arr.length
"""

#######################################################################
# Notes
#######################################################################

notes = """
Two pointers, track maximum length
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


        
s = Solution()
arr = [1,0,1,1,0, 1]
print(s.longestOnes(arr, 2))
