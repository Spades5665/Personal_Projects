# Problem: 
#   Given the head of a singly linked list, return true if it is a or false otherwise.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Find the halfway point in list
        prev = None
        slow_p = head
        fast_p = head
        while fast_p:
            prev = slow_p
            slow_p = slow_p.next
            
            # Make sure slow_pointer gets to the second half of the list
            if not fast_p.next: fast_p = fast_p.next
            else: fast_p = fast_p.next.next
        
        # Create a second head halfway into the list
        second_head = slow_p

        # Reverse the second half of the list
        while slow_p and slow_p.next:

            # Get the next two nodes
            new_head = slow_p.next
            new_next = slow_p.next.next

            # Update connections
            slow_p.next = new_next
            new_head.next = second_head

            # Update head and reconnect
            second_head = new_head
            prev.next = second_head
        
        # Loop through the new list
        while second_head:

            # Fails if the two current values arent the same
            if head.val != second_head.val: return False

            # Increment through the list
            head = head.next
            second_head = second_head.next

        # Matches were found for each value (besides center if odd)
        return True
