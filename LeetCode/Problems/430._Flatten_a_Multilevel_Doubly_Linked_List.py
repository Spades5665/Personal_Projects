# Problem:
#   You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, 
#   and an additional child pointer. This child pointer may or may not point to a separate doubly linked 
#   list, also containing these special nodes. These child lists may have one or more children of their own, 
#   and so on, to produce a multilevel data structure as shown in the example below.
#   Given the head of the first level of the list, flatten the list so that all the nodes appear in a 
#   single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list 
#   should appear after curr and before curr.next in the flattened list.
#   Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # End if no list
        if not head: return None

        # DFS traversal for the linked list
        def dfs(curr):

            # Check for child
            if curr.child: 

                # Continue until at last child
                final = dfs(curr.child)

                # Update pointer at end of childs list
                final.next = curr.next
                if curr.next: curr.next.prev = final

                # Update pointers for parent and child
                curr.next = curr.child
                curr.child.prev = curr

                # Remove child
                curr.child = None

            # Return end of the list
            elif not curr.next: return curr

            # Continue onto the next node
            return dfs(curr.next)
            
        # Call dfs on the head
        dfs(head)

        # Return new list
        return head
