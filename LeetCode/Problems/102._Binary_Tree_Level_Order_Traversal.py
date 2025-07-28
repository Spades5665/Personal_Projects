# Problem:
#   Given the root of a binary tree, return the level order traversal of its nodes' values. 
#   (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Hold level order sequence
        level_order = []

        # Add root to queue if it exists
        queue = deque([[root, 0]]) if root else None

        # Loop until queue is empty
        while queue:

            # Get next value out of queue
            node, level = queue.popleft()

            # Add level to level_order
            if level + 1 > len(level_order): level_order.append([])

            # Add value to list
            level_order[level].append(node.val)

            # Add the children of the node to the queue
            if node.left: queue.append([node.left, level + 1])
            if node.right: queue.append([node.right, level + 1])
        
        # Return list
        return level_order
