# Problem:
#   Given two strings s and t, determine if they are isomorphic.
#   Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#   All occurrences of a character must be replaced with another character while preserving 
#   the order of characters. No two characters may map to the same character, but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # Hash map to hold character mappings
        hash_map = {}

        # Loop through each letter in s
        for i in range(len(s)):

            # Check if s[i] has been mapped yet
            if s[i] not in hash_map:

                # s[i] was already mapped
                if t[i] in hash_map.values(): return False

                # Add new mapping
                else: hash_map[s[i]] = t[i]

            # Check if map is valid
            if t[i] != hash_map[s[i]]: return False
        
        # All mappings were valid
        return True
