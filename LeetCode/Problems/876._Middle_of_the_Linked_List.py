# Problem: Given the head of a singly linked list, return the middle node of the linked list.
#          If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # This part finds the total number of nodes in the linked list
        current = head
        count = 0
        while current != None:
            current = current.next
            count += 1
        
        # Finds the halfway point
        count = int(count / 2)

        # Loops to the middle
        while count > 0:
            head = head.next
            count -= 1
        
        # Returns the rest of the list from the middle
        return head
