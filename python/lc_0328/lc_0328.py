import os
import sys
from typing import Dict, List, Optional

#######################################################################
# Problem # 0328 2026-01-09 Start time: 17:01 End time:  17:18
#######################################################################
problem = """
328. Odd Even Linked List

Medium

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
"""

#######################################################################
# Notes
#######################################################################

notes = """
MISTAKES:
- Needed to check the conditions for when a node can be null
- Need to put an empty condition right at the top
- Only update the pointer if it will point to a non-null item
"""

#######################################################################
# Solution
#######################################################################

# Definition for singly-linked list.
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
    
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        odd_start: Optional[ListNode] = head
        odd_tracker: Optional[ListNode] = head
        even_start: Optional[ListNode] = head.next
        even_tracker: Optional[ListNode] = head.next


        while (odd_tracker is not None and odd_tracker.next is not None) or (even_tracker is not None and even_tracker.next is not None):
            next_even: Optional[ListNode] = None
            next_odd: Optional[ListNode] = None
            
            if even_tracker.next is not None:
                next_even = even_tracker.next.next
                
            if odd_tracker.next is not None:
                next_odd = odd_tracker.next.next

            even_tracker.next = next_even
            odd_tracker.next = next_odd
            
            if next_even is not None:
                even_tracker = next_even
            if next_odd is not None:
                odd_tracker = next_odd
            

        odd_tracker.next = even_start
        return odd_start
            


s = Solution()
a = []
ll = s.makeLinkedList(a)
print(s.printLL(s.oddEvenList(ll)))
