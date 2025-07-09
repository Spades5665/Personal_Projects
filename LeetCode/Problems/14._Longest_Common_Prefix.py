# Problem: Write a function to find the longest common prefix string amongst an array of strings.
#          If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Index and result string
        ind, pre = 0, ""

        # Find the minimum length string in strs
        minLen = len(strs[0])
        for stri in strs:
            if len(stri) < minLen:
                minLen = len(stri)

        # Loop while there are characters left to scan
        while ind < minLen:

            # Loop through each string in strs
            for i in range(len(strs) - 1):

                # Check if all strings contain the current prefix letter
                if strs[i][ind] != strs[i + 1][ind]:
                    return pre
            
            # Add letter to pre and increment
            pre += strs[0][ind]
            ind += 1

        # Return prefix string
        return pre
