# Problem:
#   You are given the heads of two sorted linked lists list1 and list2.
#   Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#   Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Pointers to traverse each list
        point_1 = list1
        point_2 = list2

        # Start the new list
        curr = None
        if (point_1 and point_2 and point_1.val <= point_2.val) or (point_1 and not point_2):
            curr = point_1
            point_1 = point_1.next
        elif point_2:
            curr = point_2
            point_2 = point_2.next
        
        # New list head
        new_head = curr

        # Loop while there is a comparison to make
        while point_1 and point_2:
            
            # Get the lower of the two
            res = point_1.val <= point_2.val

            # Find next node to add
            new_node = point_1 if res else point_2

            # Add the next node and increment curr
            curr.next = new_node
            curr = curr.next

            # Increment correct pointer
            point_1 = point_1.next if res else point_1
            point_2 = point_2.next if not res else point_2

        # Finish off list 1's values
        while point_1:
            curr.next = point_1
            curr = curr.next
            point_1 = point_1.next
        
        # Finish off list 2's values
        while point_2:
            curr.next = point_2
            curr = curr.next
            point_2 = point_2.next

        # Return the new list
        return new_head
