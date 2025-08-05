# Problem:
#   Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
#   According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes 
#   p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a 
#   descendant of itself).”

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # Find a node using bst traversal
        def bst_find(target_node):

            # Set current node
            curr = root

            # Start path
            path = [root]

            # Loop until the desired node is found
            while curr:

                # Check if node is the target
                if curr.val == target_node.val: return path

                # Find next node to traverse
                if curr.val > target_node.val:
                    path.append(curr.left)
                    curr = curr.left
                else:
                    path.append(curr.right)
                    curr = curr.right
            
            # Node not found
            return -1

        # Get the path to each node
        p_path = bst_find(p)
        q_path = bst_find(q)

        # Get the minimum possible index
        min_ind = min(len(p_path), len(q_path)) - 1

        # Loop until the common ancestor is found
        for i in range(min_ind, -1, -1):
            if p_path[i] == q_path[i]: return p_path[i]
    
        # No ancestor was found
        return None
