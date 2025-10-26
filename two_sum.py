from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Problem 1: Two Sum
        
        Given an array of integers nums and an integer target, return indices 
        of the two numbers such that they add up to target.
        
        You may assume that each input would have exactly one solution, and 
        you may not use the same element twice.
        
        You can return the answer in any order.
        
        Example 1:
            Input: nums = [2,7,11,15], target = 9
            Output: [0,1]
            Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        
        Example 2:
            Input: nums = [3,2,4], target = 6
            Output: [1,2]
        
        Example 3:
            Input: nums = [3,3], target = 6
            Output: [0,1]
        
        Constraints:
            - 2 <= nums.length <= 10^4
            - -10^9 <= nums[i] <= 10^9
            - -10^9 <= target <= 10^9
            - Only one valid answer exists
        
        Hint: Use a hash map for O(n) time complexity
        """
        # TODO: Implement your solution here
        pass


# Optional: Test locally
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    result = solution.twoSum([2, 7, 11, 15], 9)
    print(f"Test 1: {result}")  # Expected: [0, 1]
    
    # Test case 2
    result = solution.twoSum([3, 2, 4], 6)
    print(f"Test 2: {result}")  # Expected: [1, 2]
    
    # Test case 3
    result = solution.twoSum([3, 3], 6)
    print(f"Test 3: {result}")  # Expected: [0, 1]
