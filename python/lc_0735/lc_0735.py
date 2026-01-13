import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 0735 2026-01-08 Start time: 20:32 End time: 21:19
#######################################################################
problem = """
735. Asteroid Collision
Medium

We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
Example 4:

Input: asteroids = [3,5,-6,2,-1,4]​​​​​​​
Output: [-6,2,4]
Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""

#######################################################################
# Notes
#######################################################################

notes = """
Stack again

MISTAKE: 
- Updating stack_len
- Realizing asteroids keep moving until they are stopped
- I really messed this one up, the direction of asteroids also matters

FINAL:
- Took literally forever. My main mistake was using a for-loop instead of a while loop
- While loops give control that is better for stacks
"""

#######################################################################
# Solution
#######################################################################

class Solution:
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        stack_len = 0
        i = 0
        ast_len = len(asteroids)
        while (i < ast_len):
            asteroid = asteroids[i]
            if stack_len == 0:
                stack.append(asteroids[i])
                i += 1
                stack_len += 1
            else:
                last_asteroid = stack[-1]
                last_size = abs(last_asteroid)
                size = abs(asteroid)
                if last_asteroid > 0 and asteroid < 0:
                    if last_size <= size:
                        stack.pop()
                        stack_len -= 1
                    if last_size >= size:
                        i += 1
                else:
                    stack.append(asteroid)
                    stack_len += 1
                    i += 1
                    
        return stack

s = Solution()
a = [-2,2,-2,1,1]
print(s.asteroidCollision(a))
