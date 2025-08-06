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

        # Check base cases
        if not list1 and not list2: return None
        elif not list2: return list1
        elif not list1: return list2

        # Get next node and update pointers
        next_node = list1 if list1.val <= list2.val else list2
        if list1.val <= list2.val: list1 = list1.next
        else: list2 = list2.next

        # Attach next node
        next_node.next = self.mergeTwoLists(list1, list2)

        # Return node
        return next_node
