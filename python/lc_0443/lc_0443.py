import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 0443
#######################################################################
problem = """
443. String Compression
Medium

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Note: The characters in the array beyond the returned length do not matter and should be ignored.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
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
    def update_chars(self, chars, update_index, char, cnt) -> int:
        chars[update_index] = char
        update_index += 1
        if cnt > 1:
            str_cnt = str(cnt)
            for num_char in str_cnt:
                chars[update_index] = num_char
                update_index += 1
        return update_index
                     
    def compress(self, chars: List[str]) -> int:
        cnt = 1
        char = chars[0]
        update_index = 0

        for i in range(1,len(chars)):
            if chars[i] != char:
                update_index = self.update_chars(chars, update_index, char, cnt)
                cnt = 1
                char = chars[i]
            else:
                cnt += 1

        update_index = self.update_chars(chars, update_index, char,cnt)
        # Don't need +1 since it will add one for me
        return update_index

chars = ["a","a","b","b","c","c","c"]
print(chars)
s = Solution()
print(s.compress(chars))
                

            
            
            
