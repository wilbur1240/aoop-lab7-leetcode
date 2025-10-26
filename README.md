# LeetCode-Style Lab

## Problems

### Problem 1: Two Sum (35 points)
Find two numbers in an array that add up to a target value.

**File:** `two_sum.py`
**LeetCode:** [Problem 1](https://leetcode.com/problems/two-sum/)

### Problem 2: Valid Palindrome (30 points)
Check if a string is a palindrome, ignoring non-alphanumeric characters.

**File:** `valid_palindrome.py`
**LeetCode:** [Problem 125](https://leetcode.com/problems/valid-palindrome/)

### Problem 3: Merge Sorted Array (35 points)
Merge two sorted arrays in-place.

**File:** `merge_sorted.py`
**LeetCode:** [Problem 88](https://leetcode.com/problems/merge-sorted-array/)

## How to Test

1. Implement your solutions in the respective .py files
2. Run the grader:
   ```bash
   python grade.py
   ```

3. Or grade individual problems:
   ```bash
   python grade.py --problem 1
   python grade.py --problem 2
   python grade.py --problem 3
   ```

## Grading

- Total: 100 points
- Each problem has visible and hidden test cases
- Partial credit awarded for passing some tests
- Performance matters: solutions exceeding time limits will fail

## Tips

- Test locally first using the test code in each file
- Handle edge cases (empty arrays, single elements, negatives)
- Consider time complexity - aim for O(n) or O(n log n)
- Read the problem constraints carefully

Good luck!
