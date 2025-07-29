# Problem:
#   Given two integer arrays inorder and postorder where inorder is the inorder traversal of a 
#   binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # Create a dictionary holding each value in inorder and its index
        diction = {inorder[i] : i for i in range(len(inorder))}

        # Create a stack to pop values from post order
        stack = deque(postorder)

        # Construct tree recursively
        def tree(s, e):

            # Check if indices are valid
            if s > e: return None

            # Create new node
            new_node = TreeNode(stack.pop())

            # Attach children
            new_node.right = tree(diction[new_node.val] + 1, e)
            new_node.left = tree(s, diction[new_node.val] - 1)

            # Return created node
            return new_node
        
        # Return the root
        return tree(0, len(postorder) - 1)
