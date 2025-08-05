# Problem:
#   Given an integer array nums where the elements are sorted in ascending order, convert it to a 
#   height-balanced binary search tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        # Add nodes by finding middle
        def addNodes(l, h):

            # Check dimensions
            if not (0 <= l <= h < len(nums)): return None

            # Get midpoint
            m = (h + l) // 2

            # Create new node
            new_node = TreeNode(nums[m])

            # Add children
            new_node.left = addNodes(l, m - 1)
            new_node.right = addNodes(m + 1, h)

            # Return node
            return new_node
        
        # Call on root
        return addNodes(0, len(nums) - 1)
