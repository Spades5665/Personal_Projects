# Problem:
#   Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Determine if list has only one node
        if not head.next: return None

        # Pointers to traverse the list
        prev_point, end_point = head, head

        # Loop until the proper distance is formed or end of list is found
        while n > 0 and end_point.next:
            n -= 1
            end_point = end_point.next

        # If n = sz then the head needs to be removed
        if n != 0: head = head.next
        else: 

            # Loop until end_point meets the tail
            while end_point.next: 
                prev_point = prev_point.next
                end_point = end_point.next
            
            # Remove the node
            prev_point.next = prev_point.next.next

        # Return new list
        return head
