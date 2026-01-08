import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 0724 2026-01-07 Start time: 16:00 End Time: 16:04
#######################################################################
problem = """
724. Find Pivot Index
Easy

Hint
Given an array of integers arr, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: arr = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = arr[0] + arr[1] + arr[2] = 1 + 7 + 3 = 11
Right sum = arr[4] + arr[5] = 5 + 6 = 11
Example 2:

Input: arr = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: arr = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = arr[1] + arr[2] = 1 + -1 = 0
 

Constraints:

1 <= arr.length <= 104
-1000 <= arr[i] <= 1000
"""

#######################################################################
# Notes
#######################################################################

notes = """

Track sum, then add and subtract as needed
"""

#######################################################################
# Solution
#######################################################################

class Solution:
    def pivotIndex(self, arr: List[int]) -> int:

        left_sum = 0
        right_sum = sum(arr) - arr[0]
        
        if left_sum == right_sum:
            return 0

        for i in range(1,len(arr)):
            left_sum += arr[i-1]
            right_sum -= arr[i]
            
            if left_sum == right_sum:
                return i
        
        return -1
            
            
s = Solution()
a = [2,1,-1]
print(s.pivotIndex(a))

