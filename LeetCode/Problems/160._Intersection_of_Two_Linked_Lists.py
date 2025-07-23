# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # Check if the two lists are the same
        if headA == headB: return headA

        # Pointers to keep track positions in each linked list
        a_point, b_point = headA, headB
        
        # Lengths of each linked list
        a_len, b_len = 0, 0

        # Find the tail of each linked list
        while a_point.next: 
            a_point = a_point.next
            a_len += 1
        while b_point.next: 
            b_point = b_point.next
            b_len += 1

        # Reset pointers
        a_point, b_point = headA, headB

        # Equalize the sizes of the lists
        while a_len > b_len: 
            a_point = a_point.next
            a_len -= 1
        while b_len > a_len: 
            b_point = b_point.next
            b_len -= 1

        # Loop until the intersection is found
        while a_point != b_point:
            a_point = a_point.next
            b_point = b_point.next

        # Return the start of the intersection
        return a_point
