# Problem:
#   You are part of a university admissions office and need to keep track of the kth highest 
#   test score from applicants in real-time. This helps to determine cut-off marks for interviews 
#   and admissions dynamically as new applicants submit their scores.
#   You are tasked to implement a class which, for a given integer k, maintains a stream of test 
#   scores and continuously returns the kth highest test score after a new score has been submitted. 
#   More specifically, we are looking for the kth highest score in the sorted list of all scores.

class KthLargest:

    # KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
    def __init__(self, k: int, nums: List[int]):

        # Add variables
        self.nums = sorted(nums)
        self.kth_index = len(nums) - k
      
    # add(int val) Adds a new test score val to the stream and returns the element representing the kth largest 
    # element in the pool of test scores so far.
    def add(self, val: int) -> int:
        
        # Add value and resort
        self.nums.append(val)
        self.nums = sorted(self.nums)

        # Increment k and return value
        self.kth_index += 1
        return self.nums[self.kth_index]
