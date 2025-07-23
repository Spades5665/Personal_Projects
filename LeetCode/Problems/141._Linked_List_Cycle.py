# Problem:
#   Given head, the head of a linked list, determine if the linked list has a cycle in it.
#   There is a cycle in a linked list if there is some node in the list that can be reached 
#   again by continuously following the next pointer. Internally, pos is used to denote the 
#   index of the node that tail's next pointer is connected to. Note that pos is not passed
#   as a parameter.
#   Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Check if list exists
        if not head: return False

        # Pointers for traversing the list
        pointer_slow, pointer_fast = head, head.next

        # Loop until pointer_fast hits the end of the list
        while pointer_fast:

            # Check if the pointers are equal
            if pointer_fast == pointer_slow: return True
            
            # Increment the fast pointer
            if pointer_fast.next: pointer_fast = pointer_fast.next

            # Increment pointers and index
            pointer_fast = pointer_fast.next
            pointer_slow = pointer_slow.next
        
        # No loop was found
        return False
