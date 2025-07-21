# Problem:
#   You are given an integer array nums and a positive integer k.
#   A subsequence sub of nums with length x is called valid if it satisfies:
#   (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
#   Return the length of the longest valid subsequence of nums. 

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:

        # Holds each subsequence possibility and max length
        poss_mods = [[0] * k for _ in range(k)]  
        max_len = 0

        # Loop through all nums and each remainder possibility
        for num in nums:
            for prev_rem in range(k):
                
                # Add length to correct subsequence
                poss_mods[prev_rem][num % k] = poss_mods[num % k][prev_rem] + 1

                # Update max
                max_len = max(max_len, poss_mods[prev_rem][num % k])

        # Step 6: Return the maximum length found
        return max_len
      