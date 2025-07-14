# Problem: Given a reference of a node in a connected undirected graph.
#          Return a deep copy (clone) of the graph.
#          Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # Check if node exists
        if not node: return node

        # Create a new list of nodes
        newNodes = {node.val: Node(node.val, [])}

        # A stack to hold neighbors that need to be visited
        stack = deque([node])
        
        # Loop until stack is empty
        while stack:

            # Get next node and create a copy
            nextNode = stack.pop()
            clonedNode = newNodes[nextNode.val]

            # Loop through each neighbor of new node
            for neighbor in nextNode.neighbors:

                # Check if this neighbor has been cloned yet
                if neighbor.val not in newNodes:

                    # Create a new node and add it to stack
                    newNodes[neighbor.val] = Node(neighbor.val, [])
                    stack.append(neighbor)
            
                # Add neighbor to the neighbors list
                clonedNode.neighbors.append(newNodes[neighbor.val])

        # Return start of cloned graph
        return newNodes[node.val]
