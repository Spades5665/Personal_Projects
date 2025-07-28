# Problem:
#   Given the head of a linked list, rotate the list to the right by k places.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Check if no list exists or only one node
        if not head or not head.next: return head

        # First get length of the list
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        # Perform rotations if needed
        if k % n > 0:

            # Get to correct new end node
            new_end = head
            for _ in range(n - (k % n) - 1): new_end = new_end.next

            # Start new head
            new_head = new_end.next
            new_curr = new_head

            # Loop while there are nodes to move
            new_end.next = new_end.next.next
            while new_end.next:

                # Update pointers
                new_curr.next = new_end.next
                new_curr = new_curr.next

                # Move to next node
                new_end.next = new_end.next.next
                
            # Update head
            new_curr.next = head
            head = new_head

        # Return rotated list
        return head
