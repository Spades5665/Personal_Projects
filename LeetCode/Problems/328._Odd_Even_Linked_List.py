# Problem:
#   Given the head of a singly linked list, group all the nodes with odd indices together 
#   followed by the nodes with even indices, and return the reordered list.
#   The first node is considered odd, and the second node is even, and so on.
#   Note that the relative order inside both the even and odd groups should remain as it was in the input.
#   You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # No changes are needed if n < 3
        if not head or not head.next or not head.next.next: return head

        # Keep track of the last odd node and first even node
        last_odd = head
        first_even = head.next

        # Iterator to traverse list
        curr = head.next

        # Loop while there are nodes still to check
        while curr and curr.next:

            # Update last odd index node
            last_odd.next = curr.next
            last_odd = curr.next
            
            # Update current node (even)
            curr.next = curr.next.next

            # Make sure last odd connects to first even
            last_odd.next = first_even

            # Increment to the next even
            curr = curr.next

        # Return new head
        return head
