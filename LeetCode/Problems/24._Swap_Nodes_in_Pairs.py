# Problem:
#   Given a linked list, swap every two adjacent nodes and return its head. 
#   You must solve the problem without modifying the values in the list's nodes 
#   (i.e., only nodes themselves may be changed.)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
            
        # Swap nodes and reattach
        def swap(node1, node2):

            # Check if there are nodes to swap
            if node2: 
                
                # Swap nodes
                node2_next = node2.next
                node2.next = node1
                node1.next = node2_next

                # Call next
                node1.next = swap(node1.next, node1.next.next) if node1.next else None

                # Return new left node
                return node2
            
            # Return old left node
            else: return node1

        # Call swap
        return swap(head, head.next) if head else head
