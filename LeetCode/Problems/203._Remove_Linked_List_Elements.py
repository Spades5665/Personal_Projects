# Problem:
#   Given the head of a linked list and an integer val, remove all the nodes of the linked list that has 
#   Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # Iterator to traverse list
        curr = head

        # Hold the last node for pointer correcting
        prev = None

        # Loop while there is another node to check
        while curr:

            # Check if current node has the value val
            if curr.val == val: 

                # Update head if its at the head
                if curr == head: head = curr.next

                # Otherwise update previous pointer past current
                else: prev.next = curr.next
            
            # Set prev to curr if the node is good
            else: prev = curr
            
            # Move to next node
            curr = curr.next

        # Return new head
        return head
