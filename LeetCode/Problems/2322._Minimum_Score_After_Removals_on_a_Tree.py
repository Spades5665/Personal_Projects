# Problem:
#   There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
#   You are given a 0-indexed integer array nums of length n where nums[i] represents the value 
#   of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] 
#   indicates that there is an edge between nodes ai and bi in the tree.
#   Remove two distinct edges of the tree to form three connected components. For a pair of removed edges, 
#   the following steps are defined:
#   Get the XOR of all the values of the nodes for each of the three components respectively.
#   The difference between the largest XOR value and the smallest XOR value is the score of the pair.
#   For example, say the three components have the node values: [4,5,7], [1,9], and [3,3,3]. 
#   The three XOR values are 4 ^ 5 ^ 7 = 6, 1 ^ 9 = 8, and 3 ^ 3 ^ 3 = 3. The largest XOR value is 8 and 
#   the smallest XOR value is 3. The score is then 8 - 3 = 5.
#   Return the minimum score of any possible pair of edge removals on the given tree.

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        
        # Length of nums
        n = len(nums)

        # Array to hold subtree xor calculations
        subtree_XOR = [0] * n

        # Dictionary to hold each nodes neighbors
        neighbors = defaultdict(list)

        # Loop through each edge and add neighbors
        for u, v in edges: 
            neighbors[u].append(v)
            neighbors[v].append(u)

        # Keep track of sub tree nodes
        subtree_nodes = [set() for _ in range(n)]

        # Define dfs and how to handle the traversal
        def dfs_traversal(node, root):

            # Add the current node to its subtree xor value and subtree
            subtree_XOR[node] = nums[node]
            subtree_nodes[node].add(node)

            # Add each neighbor to its respective subtree xor value and subtree
            for neighbor in neighbors[node]:
                if neighbor != root:
                    dfs_traversal(neighbor, node)
                    subtree_XOR[node] ^= subtree_XOR[neighbor]
                    subtree_nodes[node].update(subtree_nodes[neighbor])

        # Initial call on root
        dfs_traversal(0, -1)

        # Get the total XOR of the whole list and initialize min_score
        total = subtree_XOR[0]
        min_score = math.inf

        # Loop through each node except root
        for i in range(1, n):

            # Loop through each edge connected to node i
            for j in range(i + 1, n):
                
                # Get the xor value of each nodes subtree
                xor_i = subtree_XOR[i]
                xor_j = subtree_XOR[j]
                
                # Get the xor value of each new subtree
                val_1 = xor_j if j in subtree_nodes[i] else xor_i
                val_2 = xor_i ^ xor_j if j in subtree_nodes[i] else xor_j ^ xor_i if i in subtree_nodes[j] else xor_j
                val_3 = total ^ xor_i if j in subtree_nodes[i] else total ^ xor_j if i in subtree_nodes[j] else total ^ xor_i ^ xor_j
                
                # Calculate score for this pair of cuts and update the minimum
                score = max(val_1, val_2, val_3) - min(val_1, val_2, val_3)
                min_score = min(min_score, score)

        # Return minimum value found
        return min_score
