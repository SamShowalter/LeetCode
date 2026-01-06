import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 0151
#######################################################################
problem = """
151. Reverse Words in a String
Medium

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
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
    WHITESPACE = {"\t"," ","\n"}

    def is_whitespace(self, char: str) -> bool:
        return char in self.WHITESPACE
    
    def get_words(self, s: str) -> List[str]:
        words: List[str] = []
        charlist: List[str] = []
        on_word: bool = False
        for char in s:
            if not self.is_whitespace(char):
                if not on_word:
                    on_word = True
                charlist.append(char)
            else:
                if on_word:
                    words.append("".join(charlist))
                    charlist = []
                    on_word = False
                    
        # If there are straggler words
        if on_word:
            words.append("".join(charlist))

        return words
        
    def reverseWords(self, s: str) -> str:
        clean_word_list: List[str] = self.get_words(s)
        return " ".join(reversed(clean_word_list))

a = "  hello world  "
s = Solution()
print(s.reverseWords(a))

