# Problem: 
#   Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
#   There is a cycle in a linked list if there is some node in the list that can be reached again by continuously 
#   following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer 
#   is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
#   Do not modify the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Check if a list exists
        if not head or not head.next: return None

        # Pointers for traversing the list
        slow_point, fast_point = head, head

        # Loop until the pointers meet
        while slow_point and fast_point and fast_point.next:

            # Increment pointers
            fast_point = fast_point.next.next
            slow_point = slow_point.next

            # End loop once they are equal
            if fast_point == slow_point: break
        
        # Check if a cycle was found
        if not fast_point == slow_point: return None

        # Reset slow point
        slow_point = head

        # Loop until poiinters meet again
        while slow_point != fast_point:
            slow_point = slow_point.next
            fast_point = fast_point.next
        
        # Return location of the start of the cycle
        return slow_point
