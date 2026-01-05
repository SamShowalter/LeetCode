import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 0605
#######################################################################
problem = """
605. Can Place Flowers

Easy

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

#######################################################################
# Notes
#######################################################################

notes = """
Find first spot where there is nothing around you, then hop 2x each time as you plant
[1,0,0,0,0,1]

Correct first try
"""

#######################################################################
# Solution
#######################################################################

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed_len = len(flowerbed)
        potential_beds = 0
        for i,f in enumerate(flowerbed):
            can_bed = (
                f == 0 # Must be empty in its position
                and (
                    i == 0 or flowerbed[i-1] == 0
                ) and (
                    i + 1 == bed_len or flowerbed[i+1] == 0
                )
            )
            if can_bed:
                flowerbed[i] = 1
                potential_beds += 1

        return n <= potential_beds

flowerbed = [1,0,0,0,0,0,1]
n = 2
s = Solution()
print(s.canPlaceFlowers(flowerbed, n))
        

