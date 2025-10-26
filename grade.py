#!/usr/bin/env python3
"""
LeetCode-Style Lab Auto-Grader
Tests three algorithm problems

Usage:
    python grade.py                    # Grade all problems
    python grade.py --problem 1        # Grade only Problem 1
    python grade.py --generate         # Generate solution templates

Problems:
    Problem 1: Two Sum (35 points)
    Problem 2: Valid Palindrome (30 points)
    Problem 3: Merge Sorted Arrays (35 points)
    Total: 100 points
"""

import sys
import os
import time
import importlib.util
from typing import Any, List, Tuple, Optional
from dataclasses import dataclass

@dataclass
class TestCase:
    """Test case with metadata"""
    input_data: dict
    expected: Any
    description: str
    points: int
    time_limit: float = 2.0
    hidden: bool = False


class LeetCodeLabGrader:
    """Auto-grader for LeetCode-style lab exercises"""
    
    def __init__(self):
        self.problems = {
            1: {
                'name': 'Two Sum',
                'file': 'two_sum.py',
                'class': 'Solution',
                'method': 'twoSum',
                'points': 35,
                'tests': []
            },
            2: {
                'name': 'Valid Palindrome',
                'file': 'valid_palindrome.py',
                'class': 'Solution',
                'method': 'isPalindrome',
                'points': 30,
                'tests': []
            },
            3: {
                'name': 'Merge Sorted Arrays',
                'file': 'merge_sorted.py',
                'class': 'Solution',
                'method': 'merge',
                'points': 35,
                'tests': []
            }
        }
        self.setup_test_cases()
    
    def setup_test_cases(self):
        """Setup test cases for all problems"""
        
        # Problem 1: Two Sum
        self.problems[1]['tests'] = [
            TestCase({'nums': [2, 7, 11, 15], 'target': 9}, 
                    [0, 1], "Basic example", 10, hidden=False),
            TestCase({'nums': [3, 2, 4], 'target': 6}, 
                    [1, 2], "Answer not at beginning", 10, hidden=False),
            TestCase({'nums': [3, 3], 'target': 6}, 
                    [0, 1], "Duplicate values", 5, hidden=False),
            TestCase({'nums': [-1, -2, -3, -4], 'target': -6}, 
                    [1, 3], "Negative numbers", 5, hidden=True),
            TestCase({'nums': list(range(1000)), 'target': 1997}, 
                    [998, 999], "Large input - performance test", 5, hidden=True, time_limit=1.0),
        ]
        
        # Problem 2: Valid Palindrome
        self.problems[2]['tests'] = [
            TestCase({'s': "A man, a plan, a canal: Panama"}, 
                    True, "Classic palindrome with punctuation", 5, hidden=False),
            TestCase({'s': "race a car"}, 
                    False, "Not a palindrome", 5, hidden=False),
            TestCase({'s': " "}, 
                    True, "Empty string (only spaces)", 5, hidden=False),
            TestCase({'s': "a."}, 
                    True, "Single character with punctuation", 5, hidden=True),
            TestCase({'s': "ab_a"}, 
                    True, "Underscore in middle", 5, hidden=True),
            TestCase({'s': "0P"}, 
                    False, "Alphanumeric check", 5, hidden=True),
        ]
        
        # Problem 3: Merge Sorted Arrays
        self.problems[3]['tests'] = [
            TestCase({'nums1': [1, 2, 3, 0, 0, 0], 'm': 3, 'nums2': [2, 5, 6], 'n': 3},
                    [1, 2, 2, 3, 5, 6], "Basic merge", 10, hidden=False),
            TestCase({'nums1': [1], 'm': 1, 'nums2': [], 'n': 0},
                    [1], "Empty nums2", 10, hidden=False),
            TestCase({'nums1': [0], 'm': 0, 'nums2': [1], 'n': 1},
                    [1], "Empty nums1", 5, hidden=False),
            TestCase({'nums1': [4, 5, 6, 0, 0, 0], 'm': 3, 'nums2': [1, 2, 3], 'n': 3},
                    [1, 2, 3, 4, 5, 6], "nums2 smaller than nums1", 5, hidden=True),
            TestCase({'nums1': [1, 2, 3, 0, 0, 0], 'm': 3, 'nums2': [4, 5, 6], 'n': 3},
                    [1, 2, 3, 4, 5, 6], "nums2 larger than nums1", 5, hidden=True),
        ]
    
    def load_solution(self, filepath: str):
        """Load Solution class from student's file"""
        if not os.path.exists(filepath):
            return None, f"File {filepath} not found"
        
        try:
            spec = importlib.util.spec_from_file_location("solution", filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            if not hasattr(module, 'Solution'):
                return None, "Solution class not found in file"
            
            return module.Solution(), None
            
        except SyntaxError as e:
            return None, f"Syntax Error: {e}"
        except Exception as e:
            return None, f"Import Error: {e}"
    
    def run_test_case(self, solution, method_name: str, test_num: int, 
                     test: TestCase) -> Tuple[str, float, str, int]:
        """
        Run a single test case
        Returns: (verdict, time_taken, message, points_earned)
        """
        # Display test info
        if test.hidden:
            print(f"    Test {test_num}: [Hidden Test] ({test.points} pts)", end=' ')
        else:
            print(f"    Test {test_num}: {test.description} ({test.points} pts)", end=' ')
        
        try:
            # Get method from solution
            if not hasattr(solution, method_name):
                print("❌")
                return "CE", 0.0, f"Method '{method_name}' not found in Solution class", 0
            
            method = getattr(solution, method_name)
            
            # Special handling for merge (modifies nums1 in-place)
            if method_name == 'merge':
                # Make a copy since merge modifies in place
                import copy
                test_input = copy.deepcopy(test.input_data)
                
                start = time.time()
                method(**test_input)
                elapsed = time.time() - start
                
                # Result is the modified nums1
                result = test_input['nums1']
            else:
                # Normal function call
                start = time.time()
                result = method(**test.input_data)
                elapsed = time.time() - start
            
            # Check time limit
            if elapsed > test.time_limit:
                print(f"❌ TLE ({elapsed*1000:.0f}ms)")
                return "TLE", elapsed, "Time Limit Exceeded", 0
            
            # Check correctness
            if result == test.expected:
                print(f"✅ ({elapsed*1000:.0f}ms)")
                return "AC", elapsed, "Correct", test.points
            else:
                print("❌ WA")
                if not test.hidden:
                    msg = f"Expected: {test.expected}, Got: {result}"
                    print(f"       Expected: {test.expected}")
                    print(f"       Got:      {result}")
                else:
                    msg = "Wrong Answer (details hidden)"
                return "WA", elapsed, msg, 0
                
        except Exception as e:
            print("❌ RE")
            msg = f"{type(e).__name__}: {e}"
            if not test.hidden:
                print(f"       Error: {msg}")
            return "RE", 0.0, msg, 0
    
    def grade_problem(self, problem_num: int) -> dict:
        """Grade a single problem"""
        problem = self.problems[problem_num]
        
        print(f"\n{'='*70}")
        print(f"Problem {problem_num}: {problem['name']} ({problem['points']} points)")
        print(f"{'='*70}")
        
        # Load solution
        print(f"  [Loading] {problem['file']}...", end=' ')
        solution, error = self.load_solution(problem['file'])
        
        if solution is None:
            print("❌")
            print(f"  {error}")
            return {
                'problem': problem_num,
                'name': problem['name'],
                'verdict': 'CE',
                'score': 0,
                'max_score': problem['points'],
                'message': error,
                'tests_passed': 0,
                'tests_total': len(problem['tests'])
            }
        
        print("✅")
        
        # Run tests
        print(f"\n  [Testing] Running {len(problem['tests'])} test cases...")
        
        results = []
        total_points = 0
        
        for i, test in enumerate(problem['tests'], 1):
            verdict, time_taken, message, points = self.run_test_case(
                solution, problem['method'], i, test
            )
            total_points += points
            results.append({
                'verdict': verdict,
                'points': points,
                'max_points': test.points,
                'message': message
            })
            
            # Stop on first failure for CE or RE
            if verdict in ['CE', 'RE']:
                break
        
        # Summary
        tests_passed = sum(1 for r in results if r['verdict'] == 'AC')
        tests_total = len(problem['tests'])
        
        print(f"\n  Result: {tests_passed}/{tests_total} tests passed")
        print(f"  Score: {total_points}/{problem['points']} points")
        
        return {
            'problem': problem_num,
            'name': problem['name'],
            'verdict': 'AC' if tests_passed == tests_total else 'Partial',
            'score': total_points,
            'max_score': problem['points'],
            'tests_passed': tests_passed,
            'tests_total': tests_total,
            'results': results
        }
    
    def grade_all(self) -> dict:
        """Grade all problems"""
        print("\n" + "="*70)
        print("  LEETCODE-STYLE LAB AUTO-GRADER")
        print("="*70)
        
        all_results = []
        total_score = 0
        total_possible = 0
        
        for prob_num in sorted(self.problems.keys()):
            result = self.grade_problem(prob_num)
            all_results.append(result)
            total_score += result['score']
            total_possible += result['max_score']
        
        # Final report
        print("\n" + "="*70)
        print("  FINAL REPORT")
        print("="*70)
        
        print(f"\n{'Problem':<30} {'Score':<20} {'Status':<20}")
        print("-"*70)
        
        for result in all_results:
            status = f"{result['tests_passed']}/{result['tests_total']} tests passed"
            score = f"{result['score']}/{result['max_score']} pts"
            print(f"Problem {result['problem']}: {result['name']:<20} {score:<20} {status:<20}")
        
        print("-"*70)
        percentage = (total_score / total_possible * 100) if total_possible > 0 else 0
        print(f"{'TOTAL':<30} {total_score}/{total_possible} pts ({percentage:.1f}%)")
        
        # Grade classification
        print("\n" + "="*70)
        if total_score == total_possible:
            print("  🎉 PERFECT SCORE! 🎉")
            print("  Excellent work!")
        elif percentage >= 90:
            print("  ✅ EXCELLENT (A)")
        elif percentage >= 80:
            print("  ✅ GOOD (B)")
        elif percentage >= 70:
            print("  ✅ SATISFACTORY (C)")
        elif percentage >= 60:
            print("  ⚠️  PASSING (D)")
        else:
            print("  ❌ NEEDS IMPROVEMENT (F)")
        print("="*70 + "\n")
        
        return {
            'total_score': total_score,
            'total_possible': total_possible,
            'percentage': percentage,
            'problems': all_results
        }


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '--problem':
            if len(sys.argv) < 3:
                print("Error: Please specify problem number (1, 2, or 3)")
                sys.exit(1)
            try:
                problem_num = int(sys.argv[2])
                if problem_num not in [1, 2, 3]:
                    print("Error: Problem number must be 1, 2, or 3")
                    sys.exit(1)
                grader = LeetCodeLabGrader()
                result = grader.grade_problem(problem_num)
                sys.exit(0 if result['verdict'] == 'AC' else 1)
            except ValueError:
                print("Error: Invalid problem number")
                sys.exit(1)
        elif sys.argv[1] in ['-h', '--help']:
            print(__doc__)
            sys.exit(0)
    
    # Grade all problems
    grader = LeetCodeLabGrader()
    result = grader.grade_all()
    
    # Exit code: 0 if passed (>= 60%), 1 otherwise
    sys.exit(0 if result['percentage'] >= 60 else 1)


if __name__ == "__main__":
    main()