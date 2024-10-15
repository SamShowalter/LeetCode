import os
import sys
from typing import Dict, List

#######################################################################
# Problem - FIRST TRY CORRECT
#######################################################################
problem = """
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
 

Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
"""

#######################################################################
# Notes
#######################################################################

notes = """
If you maintain a hashtable you will need to update all numbers
Another way would be to sort the array, then iterate throuygh and track the largest h-index
[3,0,6,1,5]


[6,5,3,1,0]
h_index
1
2
3

NOTES:
- Could have stopped the iterations earlier
- Could also have implemented a counting system with an aux array
    - Note all the indices that have an element, then count up while tracking index

"""
 

#######################################################################
# Solution
#######################################################################

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # O(nlogn)
        citations = list(reversed(sorted(citations)))

        h_index=0
        for i, num in enumerate(citations):
            h_index = max(
                min(i+1, num),
                h_index
            )
        return h_index


nums = [90,0,10,55,11,11,11]
sol = Solution()
print(sol.hIndex(nums))

        
        
 
  

