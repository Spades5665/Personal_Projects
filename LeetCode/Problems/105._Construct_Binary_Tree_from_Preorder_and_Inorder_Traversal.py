# Problem:
#   Given two integer arrays preorder and inorder where preorder is the preorder traversal of a 
#   binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Create a dictionary holding each value in inorder and its index
        diction = {inorder[i] : i for i in range(len(inorder))}

        # Create a queue to pop values from post order
        queue = deque(preorder)

        # Construct tree recursively
        def tree(s, e):

            # Check if indices are valid
            if s > e: return None

            # Create new node
            new_node = TreeNode(queue.popleft())

            # Attach children
            new_node.left = tree(s, diction[new_node.val] - 1)
            new_node.right = tree(diction[new_node.val] + 1, e)

            # Return created node
            return new_node
        
        # Return the root
        return tree(0, len(preorder) - 1)
