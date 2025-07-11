#!/usr/bin/env python3
import os
import shutil
import glob

# List of important problems for interview preparation
important_problems = [
    "1. Two Sum",
    "2. Add Two Numbers", 
    "3. Longest Substring Without Repeating Characters",
    "5. Longest Palindromic Substring",
    "11. Container With Most Water",
    "15. 3Sum",
    "20. Valid Parentheses",
    "21. Merge Two Sorted Lists",
    "26. Remove Duplicates from Sorted Array",
    "33. Search in Rotated Sorted Array",
    "53. Maximum Subarray",
    "62. Unique Paths",
    "70. Climbing Stairs",
    "78. Subsets",
    "98. Validate Binary Search Tree",
    "101. Symmetric Tree",
    "102. Binary Tree Level Order Traversal",
    "104. Maximum Depth of Binary Tree",
    "127. Word Ladder",
    "133. Clone Graph",
    "139. Word Break",
    "198. House Robber",
    "200. Number of Islands",
    "207. Course Schedule",
    "235. Lowest Common Ancestor of a Binary Search Tree",
    "242. Valid Anagram",
    "268. Missing Number",
    "283. Move Zeroes",
    "300. Longest Increasing Subsequence",
    "322. Coin Change",
    "347. Top K Frequent Elements",
    "684. Redundant Connection"
]

def copy_problem_solutions():
    """Copy all important problem solutions to mustLearn directory"""
    solutions_dir = "solutions"
    must_learn_dir = "mustLearn"
    
    # Create mustLearn directory if it doesn't exist
    os.makedirs(must_learn_dir, exist_ok=True)
    
    copied_count = 0
    
    for problem in important_problems:
        # Look for the problem directory
        problem_dir = os.path.join(solutions_dir, problem)
        if os.path.exists(problem_dir):
            # Copy Python solution if it exists
            py_file = os.path.join(problem_dir, f"{problem.split('.')[0]}.py")
            if os.path.exists(py_file):
                dest_file = os.path.join(must_learn_dir, f"{problem}.py")
                shutil.copy2(py_file, dest_file)
                print(f"✓ Copied: {problem}")
                copied_count += 1
            else:
                print(f"✗ No Python solution found for: {problem}")
        else:
            # Check if there's a direct Python file
            py_file = os.path.join(solutions_dir, f"{problem}.py")
            if os.path.exists(py_file):
                dest_file = os.path.join(must_learn_dir, f"{problem}.py")
                shutil.copy2(py_file, dest_file)
                print(f"✓ Copied: {problem}")
                copied_count += 1
            else:
                print(f"✗ Not found: {problem}")
    
    print(f"\nTotal copied: {copied_count}/{len(important_problems)}")
    
    # Also copy some additional important problems that might be named differently
    additional_problems = [
        "1. Two Sum.py",
        "20. Valid Parentheses.py",
        "70. Climbing Stairs.py",
        "98. Validate Binary Search Tree.py",
        "101. Symmetric Tree.py",
        "102. Binary Tree Level Order Traversal.py",
        "104. Maximum Depth of Binary Tree.py"
    ]
    
    for problem_file in additional_problems:
        src_file = os.path.join(solutions_dir, problem_file)
        if os.path.exists(src_file):
            dest_file = os.path.join(must_learn_dir, problem_file)
            if not os.path.exists(dest_file):  # Don't overwrite if already copied
                shutil.copy2(src_file, dest_file)
                print(f"✓ Copied additional: {problem_file}")

if __name__ == "__main__":
    copy_problem_solutions() 