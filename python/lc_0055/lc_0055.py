
import os
import sys
from typing import Dict, List

#######################################################################
# Problem
#######################################################################
problem = """
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

#######################################################################
# Notes
#######################################################################

notes = """
Sort of feels like a graph search problem. Naive solution would be to check all paths recursively
- Could there be a faster way?
- Could there be a way to do this with less memory
- What happens if you jump past the end
- Knowing the length of the array helps

"""
 

#######################################################################
# Solution
#######################################################################

class Solution:

    @staticmethod
    def _can_jump(nums, curr_index):
        if curr_index >= len(nums): return curr_index
        possible_jumps = nums[curr_index]

        curr_max = curr_index

        # For loop needed a +1 to get to the end
        for i in range(curr_index+1,curr_index + possible_jumps+1):
            
             curr_max = max(
                curr_max, 
                # BIG MISTAKE ADDING INDEX, SHOULD NOT HAVE
                # TOOK awhile to fix
                Solution._can_jump(nums, i)
            )

        return curr_max
                  
    # Takes way too long
    def canJumpBAD(self, nums: List[int]) -> bool:
        max_index = Solution._can_jump(nums, 0)
        return max_index >= len(nums) - 1

    # TIME LIMIT ALSO REACHED FOR THIS ONE, HOW TO SIMPLIFY
    def canJump(self, nums: List[int]) -> bool:
        arr_len = len(nums)
        reached = [False]*arr_len
        reached[-1] = True

        for i in reversed(range(len(nums)-1)):
            for j in range(i, min(i + nums[i]+1, arr_len)):
                if reached[min(j,arr_len)]: 
                    reached[i] = True
        
        return reached[0]

    def canJumpGas(self, nums: List[int]) -> bool:
        gas = nums[0]
        for i in range(1, len(nums)):
            if gas < 0: return False
            # Pick gas that will take you furthest
            if gas < nums[i]:
                gas = nums[i]
            gas -= 1
        return True

    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1

        for i in range(goal-1, -1,-1):
            if nums[i] + i >= goal:
                goal = i

        return goal == 0
        


    # SHOULD REVISIT, DID REALLY POORLY ON THIS

a = """
[]
 ^ - 



"""

        
nums = [3,3,0,0,4]
sol = Solution()
print(sol.canJump(nums))



