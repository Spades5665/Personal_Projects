# Problem:
#   You are given two non-empty linked lists representing two non-negative integers. 
#   The digits are stored in reverse order, and each of their nodes contains a single digit. 
#   Add the two numbers and return the sum as a linked list.
#   You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Contains the sum of the two lists
        sumList = ListNode(0)

        # Get the start of the list
        current = sumList

        # Track if added over 10
        carry = 0

        # Loop while there are still numbers to be added
        while l1 or l2 or carry > 0:
            
            # Get the sum and carry of the two numbers
            summed = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = summed // 10

            # Add the new sum to the list and increment
            current.next = ListNode(summed % 10)
            current = current.next

            # Move lists along
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the summed list
        return sumList.next
