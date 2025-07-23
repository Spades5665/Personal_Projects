# Problem:
#   Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Dictionaries to hold a counter for each number and keep track of the frequency counts
        num_counts = defaultdict(int)
        freq_counts = defaultdict(set)

        # Holds the final most frequent numbers
        most_freq = []

        # Loop through each num in nums
        for num in nums: 
            
            # Remove a num from the frequency counts if it exists
            if num in num_counts: freq_counts[num_counts[num]].remove(num)

            # Increment the counter and add the num to the correct frequency location
            num_counts[num] += 1
            freq_counts[num_counts[num]].add(num)
        
        # Reverse dictionary so max keys are searched first
        keys = list(reversed(freq_counts))
        print(keys)
        
        # Get the first k most frequent nums
        ind = 0
        while k > 0:
            while freq_counts[keys[ind]]:
                most_freq.append(freq_counts[keys[ind]].pop())
                k -= 1
            ind += 1

        # Return the k most frequent nums
        return most_freq
