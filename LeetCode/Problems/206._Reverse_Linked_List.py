# Problem:
#   Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Get current head
        curr = head

        # Loop while there is another node to reverse
        while curr and curr.next:

            # Get the next two nodes
            new_head = curr.next
            new_next = curr.next.next

            # Update connections
            curr.next = new_next
            new_head.next = head

            # Update head
            head = new_head
        
        # Return new head
        return head
