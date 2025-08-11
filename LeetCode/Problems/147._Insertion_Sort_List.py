# Problem:
#   Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Check base cases 
        if not head or not head.next: return head

        # Check every pair of values and insert 
        prev = head
        curr = head.next
        while curr:

            # Get next node to check
            next_node = curr.next

            # Check if current needs to be moved
            if curr.val < prev.val:

                # Check if new place should be head
                if curr.val < head.val:
                    prev.next = curr.next
                    curr.next = head
                    head = curr

                # Loop until proper place is found
                else:
                    old_prev = head
                    old_curr = head.next
                    while curr.val >= old_curr.val: 
                        old_prev = old_curr
                        old_curr = old_curr.next
                    
                    # Adjust pointers
                    prev.next = curr.next
                    old_prev.next = curr
                    curr.next = old_curr
            
            # No switch so update prev
            else: prev = curr
            
            # Advance to next node
            curr = next_node

        # Return the head
        return head
