import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 0392 Start time: 3:01 Finished: 3:07
#######################################################################
problem = """
392. Is Subsequence
Easy

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""

#######################################################################
# Notes
#######################################################################

notes = """
Manage two pointers and run through

Extension: I would store all the values and their positions in memory for O(1) lookup to check

"""

#######################################################################
# Solution
#######################################################################

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_t = len(t)
        len_s = len(s)
        if len_t < len_s: return False
        
        if len_s == 0: return True # Missed this edge case condition!
        
        j: int = 0
        k: int = 0

        for k in range(len_t):
            if (s[j] == t[k]):
                j += 1

            if (j == len_s): 
                return True
                
        return False
                
s = Solution()
a = "abdef"
b = "aef"
print(s.isSubsequence(b,a))
