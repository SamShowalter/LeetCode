import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 1456 Start: 3:44 End: 3:50
#######################################################################
problem = """
1456. Maximum Number of Vowels in a Substring of Given Length
Medium

Hint
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""


#######################################################################
# Notes
#######################################################################

notes = """
Can the window be larger than the array

"""

#######################################################################
# Solution
#######################################################################

class Solution:
    VOWELS = {"a","e","i","o","u"}
    def isVowel(self,char: str) -> bool:
        return char in Solution.VOWELS
        
    def maxVowels(self, s: str, k: int) -> int:
        maxCnt = sum([int(self.isVowel(s[i])) for i in range(k)])
        currCnt = maxCnt

        for i in range(k, len(s)):
            currCnt = currCnt - int(self.isVowel(s[i-k])) + int(self.isVowel(s[i]))
            maxCnt = max(maxCnt, currCnt)
            
        return maxCnt
        
s = Solution() 
a = "abciiidef"
print(s.maxVowels(a,4))

