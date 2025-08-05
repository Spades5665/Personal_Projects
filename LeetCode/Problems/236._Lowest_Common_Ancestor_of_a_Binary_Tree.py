# Problem:
#   Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#   According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined 
#   between two nodes p and q as the lowest node in T that has both p and q as descendants 
#   (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Find a node using dfs traversal
        def dfs_find(target_node):

            # Create a stack for dfs traversal
            stack = deque([[root, [root]]])

            # Loop until the desired node is found
            while stack:

                # Get next node and it's path
                node, path = stack.pop()

                # Check if node is the target
                if node.val == target_node.val: return path

                # Add children to stack
                if node.left: 
                    left_path = path.copy()
                    left_path.append(node.left)
                    stack.append([node.left, left_path])
                if node.right: 
                    right_path = path.copy()
                    right_path.append(node.right)
                    stack.append([node.right, right_path])
            
            # Node not found
            return -1

        # Get the path to each node
        p_path = dfs_find(p)
        q_path = dfs_find(q)

        # Get the minimum possible index
        min_ind = min(len(p_path), len(q_path)) - 1

        # Loop until the common ancestor is found
        for i in range(min_ind, -1, -1):
            if p_path[i] == q_path[i]: return p_path[i]
    
        # No ancestor was found
        return None
