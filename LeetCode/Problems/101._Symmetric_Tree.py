# Problem:
#   Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # Check if there is a tree to search
        if not root.left and not root.right: return True

        # Queue for bfs traversal
        queue = deque([[root.left, root.right]])

        # Loop until all nodes of each subtree have been checked
        while queue:

            # Get the next left and right to check
            left_node, right_node = queue.popleft()
            
            # If the nodes aren't equal, return false
            if not left_node or not right_node or left_node.val != right_node.val: return False

            # Add the next two nodes to check
            if left_node.left or right_node.right: queue.append([left_node.left, right_node.right])
            if left_node.right or right_node.left: queue.append([left_node.right, right_node.left])

        # All nodes were checked and passed
        return True
