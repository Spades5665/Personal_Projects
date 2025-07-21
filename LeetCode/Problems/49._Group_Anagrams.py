# Problem:
#   Given an array of strings strs, group the anagrams together. You can return the answer in any order.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # A hash table to hold sorted anagram keys
        hash_table = dict()

        # Loop through each string in strs
        for s in strs:

            # Sort the current string
            key = "".join(sorted(s))

            # Add a list to the dictionary if the key doesnt exist yet
            if key not in hash_table: hash_table[key] = [s]

            # Add to the list if it does
            else: hash_table[key].append(s)
        
        # Return the list form of the values
        return list(hash_table.values())
