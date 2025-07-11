#!/usr/bin/env python3
import os
import shutil

# Organize problems by study day
day1_problems = [
    "1. Two Sum.py",
    "20. Valid Parentheses.py", 
    "21. Merge Two Sorted Lists.py",
    "26. Remove Duplicates from Sorted Array.py",
    "53. Maximum Subarray.py",
    "70. Climbing Stairs.py",
    "98. Validate Binary Search Tree.py",
    "101. Symmetric Tree.py",
    "102. Binary Tree Level Order Traversal.py",
    "104. Maximum Depth of Binary Tree.py",
    "235. Lowest Common Ancestor of a Binary Search Tree.py"
]

day2_problems = [
    "62. Unique Paths.py",
    "127. Word Ladder.py",
    "133. Clone Graph.py",
    "139. Word Break.py",
    "198. House Robber.py",
    "200. Number of Islands.py",
    "207. Course Schedule.py",
    "300. Longest Increasing Subsequence.py",
    "322. Coin Change.py",
    "684. Redundant Connection.py"
]

day3_problems = [
    "2. Add Two Numbers.py",
    "3. Longest Substring Without Repeating Characters.py",
    "5. Longest Palindromic Substring.py",
    "11. Container With Most Water.py",
    "15. 3Sum.py",
    "33. Search in Rotated Sorted Array.py",
    "78. Subsets.py",
    "242. Valid Anagram.py",
    "268. Missing Number.py",
    "283. Move Zeroes.py",
    "347. Top K Frequent Elements.py"
]

def organize_problems():
    """Organize problems into day-specific directories"""
    base_dir = "mustLearn"
    
    # Day 1: Arrays and Trees
    day1_dir = os.path.join(base_dir, "day1_arrays_trees")
    for problem in day1_problems:
        src = os.path.join(base_dir, problem)
        dst = os.path.join(day1_dir, problem)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"✓ Day 1: {problem}")
    
    # Day 2: Dynamic Programming and Graphs
    day2_dir = os.path.join(base_dir, "day2_dp_graphs")
    for problem in day2_problems:
        src = os.path.join(base_dir, problem)
        dst = os.path.join(day2_dir, problem)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"✓ Day 2: {problem}")
    
    # Day 3: Patterns and Interview Practice
    day3_dir = os.path.join(base_dir, "day3_patterns_interview")
    for problem in day3_problems:
        src = os.path.join(base_dir, problem)
        dst = os.path.join(day3_dir, problem)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"✓ Day 3: {problem}")
    
    print(f"\nOrganized problems:")
    print(f"Day 1: {len(day1_problems)} problems")
    print(f"Day 2: {len(day2_problems)} problems") 
    print(f"Day 3: {len(day3_problems)} problems")

if __name__ == "__main__":
    organize_problems() 