# Problem:
#   Given the root of a binary tree, return all duplicate subtrees.
#   For each kind of duplicate subtrees, you only need to return the root node of any one of them.
#   Two trees are duplicate if they have the same structure with the same node values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        # Hash table to hold unique subtrees 
        hash_table = dict()

        # Holds duplicate subtrees
        duplicates = []
        
        # Traverse the tree in post order to find subtrees
        def post_order(root: Optional[TreeNode]):
            
            # Return special string if the current node is non existent
            if root is None: return "#"

            # Post order traversal
            left_val = post_order(root.left)
            right_val = post_order(root.right)
            
            # Calculate the subtree
            key = str(root.val) + "-" + left_val + "-" + right_val

            # Add the key to the table or add one if it exists
            if key not in hash_table: hash_table[key] = 1
            else: hash_table[key] += 1

            # Once a duplicate is found, add to the array
            if hash_table[key] == 2: duplicates.append(root)

            # Return the calculated key for the next node to use
            return key

        # Start the post order traversal at the root
        post_order(root)

        # Return all the duplicates
        return duplicates
