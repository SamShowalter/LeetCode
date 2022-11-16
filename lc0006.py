#################################################################################
#
#             Project Title:  LC 6
#
#################################################################################


#################################################################################
#   Module Imports
#################################################################################

import os
import sys

#################################################################################
#   Function-Class Declaration
#################################################################################

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        row_store = [[] for i in range(numRows)]

        # Make sure this corresponds to depth
        route = list(range(numRows)) + list(reversed(range(1,numRows-1)))
        for i in range(0,len(s)):
            depth = route[i % (2*(numRows - 1))]
            row_store[depth].append(s[i])

        return "".join(["".join(s) for s in row_store])



#################################################################################
#   Main Method
#################################################################################
s = Solution()
print(s.convert("paypalishiring",3))



