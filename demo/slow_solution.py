from typing import List
import time

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Slow solution - will exceed time limit
        """
        # Intentionally slow
        time.sleep(0.1)  # Simulate slow algorithm
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
