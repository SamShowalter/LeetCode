import os
import sys
from typing import List, Dict, Union

#######################################################################
# Problem
#######################################################################
problem = """
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""

#######################################################################
# Notes
#######################################################################

notes = """
- Goal is to merge the two arrays in place
- There should be no extra memory utilized besides the existing arrays

# Initial Thoughts
- Need a method to push back elements when we need to make room for a new element
- Would be nice to do this with minimal shuffles
- Naively, track through each, noting the smaller and larger elements
- We also know that the arrays are sorted, so we can take advantage of that
- I think it may be cheapest to start from the back


# Cases
- P1 empty, take all of P2
- P2 empty, just return P1
- Some mix of both
"""
 

#######################################################################
# Solution
#######################################################################


class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        - Go back to front
        """
        p = n + m -1
        p1 = m-1
        p2 = n-1

        # Cover case where nums2 empty
        if n == 0: return 

        for i in range(p,-1,-1):
            if p1 < 0 or (p2 >= 0 and nums1[p1] <= nums2[p2]):
                nums1[i] = nums2[p2]
                p2 -=1
            else:
                nums1[i] = nums1[p1]
                p1 -=1

sol = Solution()
sol.merge([1,2,99,0,0,0], 3, [5,6,11], 3)
    
#######################################################################
# Post-Submission Notes
#######################################################################

# Correct on the first try, but took a pretty long time, around 30 minutes
# Main trick was to realize that going backwards was optimal
 
  
