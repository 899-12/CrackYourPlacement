"""Given the head of a singly linked list, reverse the list, and return the
reversed list.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    prev = None
    current = head

    while current:
        next_node = current.next   # Save the next node
        current.next = prev        # Reverse the link
        prev = current             # Move prev forward
        current = next_node        # Move current forward
    
    return prev  # New head of the reversed list
