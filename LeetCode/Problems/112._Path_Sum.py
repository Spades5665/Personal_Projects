# Problem: 
#   Given the root of a binary tree and an integer targetSum, return true if the tree has a 
#   root-to-leaf path such that adding up all the values along the path equals targetSum.
#   A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # Check if root exists
        if not root: return False

        # Queue for bfs traversal
        queue = deque([[root, root.val]])

        # Loop until queue is empty
        while queue:

            # Get current node and the sum so far
            node, path_sum = queue.popleft()

            # Check if the current node is a leaf node and its sum is target sum
            if not node.left and not node.right and path_sum == targetSum: return True 

            # Add kids to queue
            if node.left: queue.append([node.left, node.left.val + path_sum])
            if node.right: queue.append([node.right, node.right.val + path_sum])
        
        # No path was found
        return False
