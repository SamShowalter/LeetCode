import os
import sys
from typing import Dict, List

#######################################################################
# Problem - READY FOR SUBMISSION, NOT SUBMITTED (FIRST TRY!!)
#######################################################################
problem = """

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
#######################################################################
# Notes
#######################################################################

notes = """
Easy to solve with a dictionary and extra space

Harder to solve with O(1) space
- Feel like you could decrement things to determine if something is majority
- [1,1,2,2,1]

KEY IDEA
- Majority of time will always happen +1 to others
- Keep track of count and current number
- Number at end will be the majority number
"""
 

#######################################################################
# Solution
#######################################################################

class Solution:
    def majorityElementDictionary(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = d.get(n,0) + 1

        for k,v, in d.items():
            if v >= (len(nums)//2 + 1):
                return k
    
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0

        for i in range(len(nums)):
            if cnt == 0:
                element = nums[i]
            if nums[i] == element:
                cnt +=1
            else:
                cnt -=1
        return element


nums = [3,2,3]

sol = Solution()
print(sol.majorityElement(nums))

                




