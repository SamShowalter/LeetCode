import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 1207 2026-01-07 Start time: 16:18 End time: 16:21
#######################################################################
problem = """
1207. Unique Number of Occurrences
Easy

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

#######################################################################
# Notes
#######################################################################

notes = """
Track with a hashtable
"""

#######################################################################
# Solution
#######################################################################

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        tracker = {}
        for a in arr:
            if a not in tracker:
                tracker[a] = 1
            else: 
                tracker[a] += 1

        return len(set(tracker.values())) == len(tracker.values())

    
a = [1,2]

s = Solution()
print(s.uniqueOccurrences(a))
