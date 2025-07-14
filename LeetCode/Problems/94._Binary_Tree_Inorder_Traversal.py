# Problem: Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Check if root exists
        if not root: return []

        # Create a stack to hold nodes to check and result array
        inorder = []
        stack = deque([root])

        # Loop until stack is empty
        while stack:

            # Get next node for checking
            current = stack[-1]

            # Check if this node has children to the left and append to stack
            while current.left and current.left not in inorder:
                current = current.left
                stack.append(current)

            # Pop the top of the stack and extract its value
            inorder.append(stack.pop())

            # Check if the node had a child to the right and add it to stack
            if current.right: stack.append(current.right)

        # Return result array
        return [x.val for x in inorder]
