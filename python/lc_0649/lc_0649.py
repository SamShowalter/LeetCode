import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 0649 2026-01-09 Start time: 09:48 End time: 10:00 First TRY!!
#######################################################################
problem = """
649. Dota2 Senate
Medium

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

 

Example 1:

Input: senate = "RD"
Output: "Radiant"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
Example 2:

Input: senate = "RDD"
Output: "Dire"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in round 1. 
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
 

Constraints:

n == senate.length
1 <= n <= 104
senate[i] is either 'R' or 'D'.
"""

#######################################################################
# Notes
#######################################################################

notes = """
Start with a count of how many Rs and Ds
Then proceed in order with a queue, tracking the number of dead in each
"""

#######################################################################
# Solution
#######################################################################

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate_len = len(senate)
        r_cnt = sum([s == 'R' for s in senate])
        d_cnt = senate_len - r_cnt
        r_dead = 0
        d_dead = 0

        dead = [False]*len(senate)
        while (d_cnt > 0 and r_cnt > 0):
            for i, s in enumerate(senate):
                if not dead[i]:
                    if senate[i] == 'R':
                        if r_dead == 0:
                            d_dead += 1
                        else:
                            dead[i] = True
                            r_cnt -= 1
                            r_dead -= 1
                    else: 
                        if d_dead == 0:
                            r_dead += 1
                        else:
                            dead[i] = True
                            d_cnt -= 1
                            d_dead -= 1
        return 'Radiant' if r_cnt > 0 else "Dire"

s = Solution()
a = "RDD"
print(s.predictPartyVictory(a))
