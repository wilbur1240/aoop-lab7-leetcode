class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Problem 2: Valid Palindrome
        
        A phrase is a palindrome if, after converting all uppercase letters 
        into lowercase letters and removing all non-alphanumeric characters, 
        it reads the same forward and backward. Alphanumeric characters include 
        letters and numbers.
        
        Given a string s, return true if it is a palindrome, or false otherwise.
        
        Example 1:
            Input: s = "A man, a plan, a canal: Panama"
            Output: true
            Explanation: "amanaplanacanalpanama" is a palindrome.
        
        Example 2:
            Input: s = "race a car"
            Output: false
            Explanation: "raceacar" is not a palindrome.
        
        Example 3:
            Input: s = " "
            Output: true
            Explanation: s is an empty string "" after removing non-alphanumeric characters.
            Since an empty string reads the same forward and backward, it is a palindrome.
        
        Constraints:
            - 1 <= s.length <= 2 * 10^5
            - s consists only of printable ASCII characters
        
        Hint: Use two pointers or clean the string first
        """
        # TODO: Implement your solution here
        pass


# Optional: Test locally
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    result = solution.isPalindrome("A man, a plan, a canal: Panama")
    print(f"Test 1: {result}")  # Expected: True
    
    # Test case 2
    result = solution.isPalindrome("race a car")
    print(f"Test 2: {result}")  # Expected: False
    
    # Test case 3
    result = solution.isPalindrome(" ")
    print(f"Test 3: {result}")  # Expected: True
