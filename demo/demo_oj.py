#!/usr/bin/env python3
"""
Mini Online Judge System - Live Demo
Simulates how LeetCode tests submissions

Usage:
    python demo_oj.py correct_solution.py    # Should pass
    python demo_oj.py wrong_solution.py      # Should fail
"""

import sys
import time
import traceback
from typing import List, Any, Callable
import importlib.util

class OnlineJudge:
    """Simulates a simple online judge like LeetCode"""
    
    def __init__(self, problem_name: str):
        self.problem_name = problem_name
        self.test_cases = []
        self.time_limit = 1.5  # seconds
        self.memory_limit = 256 * 1024 * 1024  # 256 MB
        
    def add_test_case(self, input_data: dict, expected: Any, description: str = ""):
        """Add a test case"""
        self.test_cases.append({
            'input': input_data,
            'expected': expected,
            'description': description
        })
    
    def load_solution(self, filepath: str):
        """Load Solution class from student's file"""
        try:
            spec = importlib.util.spec_from_file_location("solution", filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module.Solution()
        except Exception as e:
            return None, f"Compilation Error: {e}"
    
    def run_single_test(self, solution, test_num: int, test_case: dict):
        """Run a single test case"""
        print(f"\n{'='*60}")
        print(f"Test Case {test_num}: {test_case['description']}")
        print(f"{'='*60}")
        
        # Show input (only first 100 chars to avoid spam)
        input_str = str(test_case['input'])
        if len(input_str) > 100:
            input_str = input_str[:100] + "..."
        print(f"Input: {input_str}")
        
        try:
            # Time the execution
            start_time = time.time()
            result = solution.twoSum(**test_case['input'])
            elapsed = time.time() - start_time
            
            print(f"Your Output: {result}")
            print(f"Expected:    {test_case['expected']}")
            print(f"Time: {elapsed*1000:.2f} ms")
            
            # Check time limit
            if elapsed > self.time_limit:
                print(f"\n❌ Time Limit Exceeded")
                print(f"   Time limit: {self.time_limit}s")
                print(f"   Your time: {elapsed:.3f}s")
                return "TLE"
            
            # Check correctness
            if result == test_case['expected']:
                print(f"\n✅ PASSED")
                return "AC"
            else:
                print(f"\n❌ Wrong Answer")
                return "WA"
                
        except Exception as e:
            print(f"\n❌ Runtime Error")
            print(f"Error: {type(e).__name__}: {e}")
            print("\nTraceback:")
            traceback.print_exc()
            return "RE"
    
    def judge(self, solution_file: str):
        """Main judging function"""
        print(f"\n{'#'*60}")
        print(f"# ONLINE JUDGE - {self.problem_name}")
        print(f"{'#'*60}")
        
        # Step 1: Load solution
        print(f"\n[Step 1] Loading solution from: {solution_file}")
        solution = self.load_solution(solution_file)
        
        if solution is None:
            print("❌ Compilation Error - Cannot load solution")
            return "CE"
        
        print("✅ Solution loaded successfully")
        
        # Step 2: Run test cases
        print(f"\n[Step 2] Running {len(self.test_cases)} test cases...")
        
        results = []
        for i, test_case in enumerate(self.test_cases, 1):
            verdict = self.run_single_test(solution, i, test_case)
            results.append(verdict)
            
            # Stop on first failure (like LeetCode)
            if verdict != "AC":
                print(f"\n❌ Stopped at test case {i}")
                break
        
        # Step 3: Final verdict
        print(f"\n{'='*60}")
        print(f"FINAL VERDICT")
        print(f"{'='*60}")
        
        passed = results.count("AC")
        total = len(self.test_cases)
        
        print(f"Test Cases: {passed}/{total} passed")
        
        if all(r == "AC" for r in results):
            print(f"\n🎉 ACCEPTED 🎉")
            print(f"Congratulations! Your solution is correct.")
            return "AC"
        else:
            # Count verdict types
            verdict_counts = {}
            for v in results:
                verdict_counts[v] = verdict_counts.get(v, 0) + 1
            
            print(f"\n❌ NOT ACCEPTED")
            print(f"Verdict breakdown:")
            for verdict, count in verdict_counts.items():
                verdict_names = {
                    'AC': 'Accepted',
                    'WA': 'Wrong Answer',
                    'TLE': 'Time Limit Exceeded',
                    'RE': 'Runtime Error'
                }
                print(f"  {verdict_names[verdict]}: {count}")
            
            return results[0] if results else "CE"


def create_two_sum_judge():
    """Create judge for Two Sum problem"""
    judge = OnlineJudge("Two Sum")
    
    # Test Case 1: Basic example
    judge.add_test_case(
        input_data={'nums': [2, 7, 11, 15], 'target': 9},
        expected=[0, 1],
        description="Basic case from problem statement"
    )
    
    # Test Case 2: Different order
    judge.add_test_case(
        input_data={'nums': [3, 2, 4], 'target': 6},
        expected=[1, 2],
        description="Answer not at beginning"
    )
    
    # Test Case 3: Duplicate numbers
    judge.add_test_case(
        input_data={'nums': [3, 3], 'target': 6},
        expected=[0, 1],
        description="Duplicate numbers"
    )
    
    # Test Case 4: Negative numbers
    judge.add_test_case(
        input_data={'nums': [-1, -2, -3, -4, -5], 'target': -8},
        expected=[2, 4],
        description="Negative numbers"
    )
    
    # Test Case 5: Large input (performance test)
    large_nums = list(range(10000))
    judge.add_test_case(
        input_data={'nums': large_nums, 'target': 19997},
        expected=[9998, 9999],
        description="Large input - performance test"
    )
    
    return judge


def generate_example_solutions():
    """Generate example solution files for demo"""
    
    # Correct solution
    correct_solution = '''from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Correct solution using hash map
        Time: O(n), Space: O(n)
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
'''
    
    # Wrong solution (incorrect logic)
    wrong_solution = '''from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Wrong solution - returns wrong indices
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i+1, j+1]  # BUG: Off by one!
        return []
'''
    
    # Slow solution (will TLE on large input)
    slow_solution = '''from typing import List
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
'''
    
    # Runtime error solution
    error_solution = '''from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Solution with runtime error
        """
        return nums[100000]  # Index out of bounds!
'''
    
    # Write files
    with open('correct_solution.py', 'w') as f:
        f.write(correct_solution)
    
    with open('wrong_solution.py', 'w') as f:
        f.write(wrong_solution)
    
    with open('slow_solution.py', 'w') as f:
        f.write(slow_solution)
    
    with open('error_solution.py', 'w') as f:
        f.write(error_solution)
    
    print("Generated example solutions:")
    print("  ✅ correct_solution.py - Should get AC")
    print("  ❌ wrong_solution.py - Should get WA")
    print("  ⏱️  slow_solution.py - Should get TLE")
    print("  💥 error_solution.py - Should get RE")


def main():
    if len(sys.argv) < 2:
        print("Mini Online Judge System")
        print("=" * 60)
        print("\nUsage:")
        print("  python demo_oj.py <solution_file>")
        print("\nOr generate example solutions:")
        print("  python demo_oj.py --generate")
        print("\nThen test them:")
        print("  python demo_oj.py correct_solution.py")
        print("  python demo_oj.py wrong_solution.py")
        sys.exit(1)
    
    if sys.argv[1] == '--generate':
        generate_example_solutions()
        print("\nNow you can test them:")
        print("  python demo_oj.py correct_solution.py")
        sys.exit(0)
    
    # Create judge and run
    solution_file = sys.argv[1]
    judge = create_two_sum_judge()
    verdict = judge.judge(solution_file)
    
    # Exit with appropriate code (for automated grading)
    sys.exit(0 if verdict == "AC" else 1)


if __name__ == "__main__":
    main()