import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 2130 2026-01-11 Start time: 12:30 End time: 12:34 (Nailed IT!!)
#######################################################################
problem = """
2130. Maximum Twin Sum of a Linked List
Medium

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 

Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105
"""

#######################################################################
# Notes
#######################################################################

notes = """
Store in a stack and then pop off one at a time and track total
"""

#######################################################################
# Solution
#######################################################################


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def makeLinkedList(self, arr: List[int]) -> Optional[ListNode]:
        if len(arr) == 0: return None
        head = ListNode(arr[0])
        tracker = head
        for i in range(1, len(arr)):
            tracker.next = ListNode(arr[i])
            tracker = tracker.next
        return head

    def printLL(self, head: Optional[ListNode]) -> str:
        s = ""
        while head != None:
            s += f"{head.val} -> "
            head = head.next
        return s
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        tracker = head
        data = []
        list_len = 0

        while tracker is not None:
            list_len += 1
            data.append(tracker.val)
            tracker = tracker.next

        half = len(data) // 2

        return max([a+b for a,b in zip(data[:half], reversed(data[half:]))])

        
s = Solution()
a= [4,2,2,3]
ll = s.makeLinkedList(a)
print(s.pairSum(ll))
    
