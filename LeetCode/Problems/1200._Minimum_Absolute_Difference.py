# Problem:
#   Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
#   Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
#   a, b are from arr
#   a < b
#   b - a equals to the minimum absolute difference of any two elements in arr

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        # Sort array
        arr = sorted(arr)

        # Find minimum difference
        min_diff = 10 ** 6 + 1
        for i in range(len(arr) - 1): min_diff = min(min_diff, arr[i + 1] - arr[i])

        # Find each pair that has the min diff
        ans = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_diff: ans.append([arr[i], arr[i + 1]])
        
        # Return answer
        return ans
