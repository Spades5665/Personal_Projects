# Problem:
#   Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST).
#   Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the 
#   smallest element in the BST.
#   You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order 
#   traversal when next() is called.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    # BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. 
    # The root of the BST is given as part of the constructor. The pointer should 
    # be initialized to a non-existent number smaller than any element in the BST.
    def __init__(self, root: Optional[TreeNode]):
        
        # Hold an array made from in order traversal
        self.in_order = []

        # Recursively traverse tree
        def inOrderTraversal(node):

            # Check for left child
            if node.left: inOrderTraversal(node.left)

            # Collect node's value
            self.in_order.append(node.val)

            # Check for right child
            if node.right: inOrderTraversal(node.right)

        # Call on root if root exists
        if root: inOrderTraversal(root)

        # Initialize index
        self.ind = -1

    # next() Moves the pointer to the right, then returns the number at the pointer.
    def next(self) -> int:

        # Return the next value and increment
        self.ind += 1
        return self.in_order[self.ind]
        
    # hasNext() Returns true if there exists a number in the traversal to the right 
    # of the pointer, otherwise returns false.
    def hasNext(self) -> bool:

        # Check index
        return self.ind + 1 < len(self.in_order)
