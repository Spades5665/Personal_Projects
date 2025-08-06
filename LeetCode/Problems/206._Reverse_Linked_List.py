# Problem:
#   Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Check if head or its next node exists
        if not head or not head.next: return head

        # Recursively call on next
        new_head = self.reverseList(head.next)

        # Update pointers
        head.next.next = head
        head.next = None

        # Return new head
        return new_head
