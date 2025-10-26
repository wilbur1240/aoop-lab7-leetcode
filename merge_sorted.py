from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Problem 3: Merge Sorted Array
        
        You are given two integer arrays nums1 and nums2, sorted in non-decreasing 
        order, and two integers m and n, representing the number of elements in 
        nums1 and nums2 respectively.
        
        Merge nums2 into nums1 as one sorted array.
        
        The final sorted array should not be returned by the function, but instead 
        be stored inside the array nums1. To accommodate this, nums1 has a length 
        of m + n, where the first m elements denote the elements that should be 
        merged, and the last n elements are set to 0 and should be ignored. 
        nums2 has a length of n.
        
        Example 1:
            Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
            Output: [1,2,2,3,5,6]
            Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
            The result of the merge is [1,2,2,3,5,6].
        
        Example 2:
            Input: nums1 = [1], m = 1, nums2 = [], n = 0
            Output: [1]
            Explanation: The arrays we are merging are [1] and [].
            The result of the merge is [1].
        
        Example 3:
            Input: nums1 = [0], m = 0, nums2 = [1], n = 1
            Output: [1]
            Explanation: The arrays we are merging are [] and [1].
            The result of the merge is [1].
        
        Constraints:
            - nums1.length == m + n
            - nums2.length == n
            - 0 <= m, n <= 200
            - 1 <= m + n <= 200
            - -10^9 <= nums1[i], nums2[j] <= 10^9
        
        Hint: Merge from the end to avoid overwriting elements
        
        Note: Do not return anything, modify nums1 in-place instead.
        """
        # TODO: Implement your solution here
        pass


# Optional: Test locally
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    solution.merge(nums1, 3, nums2, 3)
    print(f"Test 1: {nums1}")  # Expected: [1, 2, 2, 3, 5, 6]
    
    # Test case 2
    nums1 = [1]
    nums2 = []
    solution.merge(nums1, 1, nums2, 0)
    print(f"Test 2: {nums1}")  # Expected: [1]
    
    # Test case 3
    nums1 = [0]
    nums2 = [1]
    solution.merge(nums1, 0, nums2, 1)
    print(f"Test 3: {nums1}")  # Expected: [1]
