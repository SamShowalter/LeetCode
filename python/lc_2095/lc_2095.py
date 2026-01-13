import os
import sys
import copy
from typing import Dict, List

#######################################################################
# Problem # 2095 2026-01-09 Start time: 11:09 End time: 11:25
#######################################################################
problem = """
2095. Delete the Middle Node of a Linked List
Medium

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
 

Constraints:

The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105
"""

#######################################################################
# Notes
#######################################################################

notes = """
Found the length of the list first, then jumped to it

Alternatively, you could jump 2 at a time v one at a time to get middle node
- This is MUCH faster
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
        
    def getListLen(self, head: Optional[ListNode]) -> int:
        size = 0
        while head != None:
            size += 1
            head = head.next
        return size
            
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tracker = head
        list_size = self.getListLen(tracker)
        middle_node = int(list_size/2)
        if middle_node == 0:
            # ERROR: This should return None, 
            return None

        i = 0
        tracker = head
        for i in range(middle_node-1):
            tracker = tracker.next
            i += 1
        node_to_delete = tracker.next
        tracker.next = node_to_delete.next
        return head

a = []
s = Solution()
ll = s.makeLinkedList(a)
print(s.printLL(ll))
print(s.printLL(s.deleteMiddle(ll)))

