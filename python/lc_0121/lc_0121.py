import os
import sys
from typing import Dict, List

#######################################################################
# Problem (READY TO SUBMIT)
#######################################################################
problem = """

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

#######################################################################
# Notes
#######################################################################

notes = """

Need to find the elements with the max diff where smallest element occurs first
- Naively, you could try all combinations (element, then max of others)
    - O(n^2)
- Is there a way to do it linearly? (yes)
    - Could keep a min heap of values seen before and look at max profit O(nlog(n))
- Is there a way to do it linear time and constant space?
    - Maybe DP could help?
    - track previous min value
    - track current max profit

"""
 

#######################################################################
# Solution
#######################################################################

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            curr_price = prices[i]
            profit = max(curr_price - curr_min, 0)
            max_profit = max(profit, max_profit)
            curr_min = min(curr_min, curr_price)

        return max_profit
            
prices = [7,6,3,1, 9,99,10,31, 9999]
sol = Solution()
print(sol.maxProfit(prices))
