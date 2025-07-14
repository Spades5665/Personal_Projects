# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
        # Store string version of the number
        num = ""

        # Loop through each node and add current element to string
        while head:
            num += str(head.val)
            head = head.next

        # Return the converted number
        return int(num, 2)
