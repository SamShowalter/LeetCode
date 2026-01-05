import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 0345
#######################################################################
problem = """
345. Reverse Vowels of a String
Easy

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""

#######################################################################
# Notes
#######################################################################

notes = """
Scan through the string and isolate vowels and their indices separately
Then, reverse the vowels, but keep indices the same, and replace them all

MISTAKE: s.split() does not split string, need list(s)
"""

#######################################################################
# Solution
#######################################################################

class Solution:
    VOWELS = set({'a','e','i','o','u'})
    def is_vowel(self, char: str):
        return char.lower() in Solution.VOWELS
        
    def reverseVowels(self, s: str) -> str:
        vowels: List[str] = []
        vowel_inds: List[int] = []
        s_list: List[str] = list(s)

        for i, char in enumerate(s_list):
            if self.is_vowel(char):
                vowel_inds.append(i)
                vowels.insert(0,char)
        
        for ind, v in zip(vowel_inds, vowels):
            s_list[ind] = v
            
        return "".join(s_list)

s = Solution()
print(s.reverseVowels("leetcode"))

        
