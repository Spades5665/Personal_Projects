# Problem:
#   Given an integer n, return all the structurally unique BST's (binary search trees), 
#   which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        # Helper function to generate trees
        def genTrees(s, e):

            # Check for good values
            if s > e: return [None, ]

            # Keep track of all trees
            trees = []

            # Loop through each index between start and end
            for i in range(s, e + 1):

                # Get the trees of the children
                l_trees = genTrees(s, i - 1)
                r_trees = genTrees(i + 1, e)

                # Setup connections
                for l in l_trees:
                    for r in r_trees:

                        # Create current tree to update connections
                        curr = TreeNode(i)
                        curr.left = l
                        curr.right = r
                        
                        # Add to all trees
                        trees.append(curr)
                
            # Return trees
            return trees
        
        # Call on base
        return genTrees(1, n)
