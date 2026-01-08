import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 1657 2026-01-07 Start time: 16:21 End Time: 16:27
#######################################################################
problem = """
1657. Determine if Two Strings Are Close
Medium

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
 

Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
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
    
    def makeCntDict(self, word):
        tracker = {}
        for w in word:
            if w not in tracker:
                tracker[w] = 1
            else:
                tracker[w] += 1
        return tracker

    def op1_check(self, word1, word2) -> bool:
        return len(word1) == len(word2) and set(word1) == set(word2)

        
    def op2_check(self, word1, word2) -> bool:
        t1 = self.makeCntDict(word1)
        t2 = self.makeCntDict(word2)

        return (
            list(sorted(t1.values())) == list(sorted(t2.values())) and
                len(t1.keys()) == len(t2.keys())
        )
        # If counts are same and number of unique values is same, then we are good
    
        
    def closeStrings(self, word1: str, word2: str) -> bool:
        return self.op1_check(word1,word2) and self.op2_check(word1,word2)
    
        
word1 = "bca"; word2 = "abc"
s = Solution()
print(s.closeStrings(word1, word2))
