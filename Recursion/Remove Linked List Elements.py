"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head."""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node to handle cases where head needs to be removed
        dummy = ListNode(0)
        dummy.next = head

        current = dummy
        while current and current.next:
            if current.next.val == val:
                # Skip the node
                current.next = current.next.next
            else:
                # Move to next node
                current = current.next

        return dummy.next
            
