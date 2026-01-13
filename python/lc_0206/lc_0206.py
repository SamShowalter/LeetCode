import os
import sys
from typing import Dict, List

#######################################################################
# Problem # 0206 2026-01-10 Start time: 17:19 End time: 17:27
#######################################################################
problem = """
206. Reverse Linked List
Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.
 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""

#######################################################################
# Notes
#######################################################################

notes = """

Mistake:
- Got indices messed up, will need to be more careful in a real interview
- mid.next = start
- Should go until lead is None for first time
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
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        start, mid, lead = head, head.next, head.next.next
        start.next = None

        while (lead is not None):
            mid.next = start
            start = mid
            mid = lead
            lead = lead.next
            
        mid.next = start
        return mid
        
s = Solution()
a = [1,2,3,4,5]
ll = s.makeLinkedList(a)
print(s.printLL(s.reverseList(ll)))
