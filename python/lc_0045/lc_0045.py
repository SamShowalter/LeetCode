
import os
import sys
from typing import Dict, List

#######################################################################
# Problem - HAD TO LOOK AT SOLUTIONS
#######################################################################
TITLE = "Jump Game II"
problem = """ 
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

#######################################################################
# Notes
#######################################################################

notes = """

[2,3,1,1,4]

[0,1,1,0,2]

[3,1,8,1,1,1,1,1,1,0]
[0,2,1,6,5,4,3,2,1,0]

[0,1,2,1,0]

"""
 

#######################################################################
# Solution
#######################################################################

class Solution:
    def jumpBackToFront(self, nums: List[int]) -> int:
        arr_len = len(nums)
        min_steps = [0]*arr_len
        current_min = float("inf")
        for i in range(arr_len-2, -1,-1):
            max_jump = min(arr_len-1, i + nums[i])
            min_steps[i] = 1 + min_steps[max_jump]
            
        return min_steps[0]
    
    def jumpKeepTrackWRONG(self, nums: List[int]) -> int:
        arr_len = len(nums)
        jumps = [float('inf')]*arr_len
        for i in range(arr_len):
            prior_value = 0 if i == 0 else jumps[i-1]
            jumps[i] = min(prior_value + 1, jumps[i])
            # Furthest jump you can make
            index = int(min(arr_len-1, i + nums[i]))
            jumps[index] = min(jumps[i],jumps[index])
            if index == arr_len-1:
                break
        print(jumps)
        return jumps[index]

    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        current_furthest = 0
        jumps = 0
        furthest = 0

        """
        [2,3,1,1,4]
        0, 0, 0
        2, 1, 2
        4, 1, 2
        4, 2, 4

        Makes sense, the idea is that:
        - Iterate through list
        - Keep track of furthest point you can get to in your position
        - Also keep track of the furthest point in general
        - When you hit your current furthest point, you know you need to add
          another jump to go further. You may have already found a faster way, 
          but that means you jumped again earlier, hence getting another jump
        
        
        """
        for i in range(len(nums)-1): # Need this for the case where there is length one list
            current_furthest = max(current_furthest,nums[i] + i)
            if i == furthest:
                jumps += 1
                furthest = current_furthest
                if furthest >= len(nums)-1:
                    break
                
        return jumps
                

            
            
            
        
nums = [2,3,1,1,4]
sol = Solution()
print(sol.jump(nums))
