# Problem:
#   Given a binary tree
#   Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#   Initially, all next pointers are set to NULL.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        # A dictionary to hold each level
        level_dict = defaultdict(list)

        # A queue to collect all nodes in the tree
        queue = deque([[root, 0]]) if root else None

        # Loop until queue is empty
        while queue:

            # Get next node and it's level
            node, level = queue.popleft()

            # Update pointer of last node if it exists
            if level in level_dict: level_dict[level][-1].next = node

            # Update node's next pointer and add it to the dictionary
            node.next = None
            level_dict[level].append(node)

            # Add children to queue
            if node.left: queue.append([node.left, level + 1])
            if node.right: queue.append([node.right, level + 1])
        
        # Return root
        return root
