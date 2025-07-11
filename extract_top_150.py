#!/usr/bin/env python3
"""
Script to extract all solutions for Top 150 Interview problems
and organize them in a single folder without nested directories.
"""

import json
import os
import shutil
import re
from pathlib import Path

# Top 150 Interview problems list
TOP_150_PROBLEMS = [
    # Array / String
    "88. Merge Sorted Array",
    "27. Remove Element", 
    "26. Remove Duplicates from Sorted Array",
    "80. Remove Duplicates from Sorted Array II",
    "169. Majority Element",
    "189. Rotate Array",
    "121. Best Time to Buy and Sell Stock",
    "122. Best Time to Buy and Sell Stock II",
    "55. Jump Game",
    "45. Jump Game II",
    "274. H-Index",
    "380. Insert Delete GetRandom O(1)",
    "238. Product of Array Except Self",
    "134. Gas Station",
    "135. Candy",
    "42. Trapping Rain Water",
    "13. Roman to Integer",
    "12. Integer to Roman",
    "58. Length of Last Word",
    "14. Longest Common Prefix",
    "151. Reverse Words in a String",
    "6. ZigZag Conversion",
    "28. Find the Index of the First Occurrence in a String",
    "68. Text Justification",
    
    # Two Pointers
    "125. Valid Palindrome",
    "392. Is Subsequence",
    "167. Two Sum II - Input Array Is Sorted",
    "11. Container With Most Water",
    "15. 3Sum",
    
    # Sliding Window
    "209. Minimum Size Subarray Sum",
    "3. Longest Substring Without Repeating Characters",
    "30. Substring with Concatenation of All Words",
    "76. Minimum Window Substring",
    
    # Matrix
    "36. Valid Sudoku",
    "54. Spiral Matrix",
    "48. Rotate Image",
    "73. Set Matrix Zeroes",
    "289. Game of Life",
    
    # Hashmap
    "383. Ransom Note",
    "205. Isomorphic Strings",
    "290. Word Pattern",
    "242. Valid Anagram",
    "49. Group Anagrams",
    "1. Two Sum",
    "202. Happy Number",
    "219. Contains Duplicate II",
    "128. Longest Consecutive Sequence",
    
    # Intervals
    "228. Summary Ranges",
    "56. Merge Intervals",
    "57. Insert Interval",
    "452. Minimum Number of Arrows to Burst Balloons",
    
    # Stack
    "20. Valid Parentheses",
    "71. Simplify Path",
    "155. Min Stack",
    "150. Evaluate Reverse Polish Notation",
    "224. Basic Calculator",
    
    # Linked List
    "141. Linked List Cycle",
    "2. Add Two Numbers",
    "21. Merge Two Sorted Lists",
    "138. Copy List with Random Pointer",
    "92. Reverse Linked List II",
    "25. Reverse Nodes in k-Group",
    "19. Remove Nth Node From End of List",
    "82. Remove Duplicates from Sorted List II",
    "61. Rotate List",
    "86. Partition List",
    "146. LRU Cache",
    
    # Binary Tree General
    "104. Maximum Depth of Binary Tree",
    "100. Same Tree",
    "226. Invert Binary Tree",
    "101. Symmetric Tree",
    "105. Construct Binary Tree from Preorder and Inorder Traversal",
    "106. Construct Binary Tree from Inorder and Postorder Traversal",
    "117. Populating Next Right Pointers in Each Node II",
    "114. Flatten Binary Tree to Linked List",
    "112. Path Sum",
    "129. Sum Root to Leaf Numbers",
    "124. Binary Tree Maximum Path Sum",
    "173. Binary Search Tree Iterator",
    "222. Count Complete Tree Nodes",
    "236. Lowest Common Ancestor of a Binary Tree",
    
    # Binary Tree BFS
    "199. Binary Tree Right Side View",
    "637. Average of Levels in Binary Tree",
    "102. Binary Tree Level Order Traversal",
    "103. Binary Tree Zigzag Level Order Traversal",
    
    # Binary Search Tree
    "530. Minimum Absolute Difference in BST",
    "230. Kth Smallest Element in a BST",
    "98. Validate Binary Search Tree",
    
    # Graph General
    "200. Number of Islands",
    "130. Surrounded Regions",
    "133. Clone Graph",
    "399. Evaluate Division",
    "207. Course Schedule",
    "210. Course Schedule II",
    
    # Graph BFS
    "909. Snakes and Ladders",
    "433. Minimum Genetic Mutation",
    "127. Word Ladder",
    
    # Trie
    "208. Implement Trie (Prefix Tree)",
    "211. Design Add and Search Words Data Structure",
    "212. Word Search II",
    
    # Backtracking
    "17. Letter Combinations of a Phone Number",
    "77. Combinations",
    "46. Permutations",
    "39. Combination Sum",
    "52. N-Queens II",
    "22. Generate Parentheses",
    "79. Word Search",
    
    # Divide & Conquer
    "108. Convert Sorted Array to Binary Search Tree",
    "148. Sort List",
    "427. Construct Quad Tree",
    "23. Merge k Sorted Lists",
    
    # Kadane's Algorithm
    "53. Maximum Subarray",
    "918. Maximum Sum Circular Subarray",
    
    # Binary Search
    "35. Search Insert Position",
    "74. Search a 2D Matrix",
    "162. Find Peak Element",
    "33. Search in Rotated Sorted Array",
    "34. Find First and Last Position of Element in Sorted Array",
    "153. Find Minimum in Rotated Sorted Array",
    "4. Median of Two Sorted Arrays",
    
    # Heap
    "215. Kth Largest Element in an Array",
    "502. IPO",
    "373. Find K Pairs with Smallest Sums",
    "295. Find Median from Data Stream",
    
    # Bit Manipulation
    "67. Add Binary",
    "190. Reverse Bits",
    "191. Number of 1 Bits",
    "136. Single Number",
    "137. Single Number II",
    "201. Bitwise AND of Numbers Range",
    
    # Math
    "9. Palindrome Number",
    "66. Plus One",
    "172. Factorial Trailing Zeroes",
    "69. Sqrt(x)",
    "50. Pow(x, n)",
    "149. Max Points on a Line",
    
    # 1D DP
    "70. Climbing Stairs",
    "198. House Robber",
    "139. Word Break",
    "322. Coin Change",
    "300. Longest Increasing Subsequence",
    
    # Multidimensional DP
    "120. Triangle",
    "64. Minimum Path Sum",
    "63. Unique Paths II",
    "5. Longest Palindromic Substring",
    "97. Interleaving String",
    "72. Edit Distance",
    "123. Best Time to Buy and Sell Stock III",
    "188. Best Time to Buy and Sell Stock IV",
    "221. Maximal Square"
]

def extract_problem_number(title):
    """Extract problem number from title."""
    match = re.match(r'(\d+)\.', title)
    return int(match.group(1)) if match else None

def find_solution_files(problem_title, solutions_dir):
    """Find all solution files for a given problem."""
    problem_number = extract_problem_number(problem_title)
    if not problem_number:
        return []
    
    # Look for the problem directory
    problem_dir = None
    for item in os.listdir(solutions_dir):
        if item.startswith(f"{problem_number}."):
            problem_dir = os.path.join(solutions_dir, item)
            break
    
    if not problem_dir or not os.path.isdir(problem_dir):
        return []
    
    solution_files = []
    for file in os.listdir(problem_dir):
        if file.endswith(('.py', '.cpp', '.java', '.js')):
            solution_files.append(os.path.join(problem_dir, file))
    
    return solution_files

def copy_solutions_to_top_150():
    """Copy all Top 150 solutions to the new folder."""
    solutions_dir = "solutions"
    target_dir = "top_interview_150"
    
    if not os.path.exists(solutions_dir):
        print(f"Solutions directory '{solutions_dir}' not found!")
        return
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    copied_count = 0
    missing_count = 0
    
    for problem in TOP_150_PROBLEMS:
        problem_number = extract_problem_number(problem)
        if not problem_number:
            print(f"Could not extract problem number from: {problem}")
            continue
        
        solution_files = find_solution_files(problem, solutions_dir)
        
        if not solution_files:
            print(f"❌ No solutions found for: {problem}")
            missing_count += 1
            continue
        
        # Copy each solution file
        for solution_file in solution_files:
            filename = os.path.basename(solution_file)
            # Create a clean filename with problem number and language
            lang = os.path.splitext(filename)[1]
            clean_filename = f"{problem_number}_{problem.replace(' ', '_').replace('.', '')}{lang}"
            
            target_file = os.path.join(target_dir, clean_filename)
            
            try:
                shutil.copy2(solution_file, target_file)
                print(f"✅ Copied: {problem} -> {clean_filename}")
                copied_count += 1
            except Exception as e:
                print(f"❌ Failed to copy {solution_file}: {e}")
    
    print(f"\n📊 Summary:")
    print(f"✅ Successfully copied: {copied_count} files")
    print(f"❌ Missing solutions: {missing_count} problems")
    print(f"📁 Target directory: {target_dir}")

def create_readme():
    """Create a README file for the Top 150 folder."""
    readme_content = """# Top 150 Interview Problems

This folder contains solutions for the Top 150 most important LeetCode problems for technical interviews.

## Organization

Problems are organized by category:

### Array / String
- Merge Sorted Array (88)
- Remove Element (27)
- Remove Duplicates from Sorted Array (26)
- Remove Duplicates from Sorted Array II (80)
- Majority Element (169)
- Rotate Array (189)
- Best Time to Buy and Sell Stock (121)
- Best Time to Buy and Sell Stock II (122)
- Jump Game (55)
- Jump Game II (45)
- H-Index (274)
- Insert Delete GetRandom O(1) (380)
- Product of Array Except Self (238)
- Gas Station (134)
- Candy (135)
- Trapping Rain Water (42)
- Roman to Integer (13)
- Integer to Roman (12)
- Length of Last Word (58)
- Longest Common Prefix (14)
- Reverse Words in a String (151)
- ZigZag Conversion (6)
- Find the Index of the First Occurrence in a String (28)
- Text Justification (68)

### Two Pointers
- Valid Palindrome (125)
- Is Subsequence (392)
- Two Sum II - Input Array Is Sorted (167)
- Container With Most Water (11)
- 3Sum (15)

### Sliding Window
- Minimum Size Subarray Sum (209)
- Longest Substring Without Repeating Characters (3)
- Substring with Concatenation of All Words (30)
- Minimum Window Substring (76)

### Matrix
- Valid Sudoku (36)
- Spiral Matrix (54)
- Rotate Image (48)
- Set Matrix Zeroes (73)
- Game of Life (289)

### Hashmap
- Ransom Note (383)
- Isomorphic Strings (205)
- Word Pattern (290)
- Valid Anagram (242)
- Group Anagrams (49)
- Two Sum (1)
- Happy Number (202)
- Contains Duplicate II (219)
- Longest Consecutive Sequence (128)

### Intervals
- Summary Ranges (228)
- Merge Intervals (56)
- Insert Interval (57)
- Minimum Number of Arrows to Burst Balloons (452)

### Stack
- Valid Parentheses (20)
- Simplify Path (71)
- Min Stack (155)
- Evaluate Reverse Polish Notation (150)
- Basic Calculator (224)

### Linked List
- Linked List Cycle (141)
- Add Two Numbers (2)
- Merge Two Sorted Lists (21)
- Copy List with Random Pointer (138)
- Reverse Linked List II (92)
- Reverse Nodes in k-Group (25)
- Remove Nth Node From End of List (19)
- Remove Duplicates from Sorted List II (82)
- Rotate List (61)
- Partition List (86)
- LRU Cache (146)

### Binary Tree General
- Maximum Depth of Binary Tree (104)
- Same Tree (100)
- Invert Binary Tree (226)
- Symmetric Tree (101)
- Construct Binary Tree from Preorder and Inorder Traversal (105)
- Construct Binary Tree from Inorder and Postorder Traversal (106)
- Populating Next Right Pointers in Each Node II (117)
- Flatten Binary Tree to Linked List (114)
- Path Sum (112)
- Sum Root to Leaf Numbers (129)
- Binary Tree Maximum Path Sum (124)
- Binary Search Tree Iterator (173)
- Count Complete Tree Nodes (222)
- Lowest Common Ancestor of a Binary Tree (236)

### Binary Tree BFS
- Binary Tree Right Side View (199)
- Average of Levels in Binary Tree (637)
- Binary Tree Level Order Traversal (102)
- Binary Tree Zigzag Level Order Traversal (103)

### Binary Search Tree
- Minimum Absolute Difference in BST (530)
- Kth Smallest Element in a BST (230)
- Validate Binary Search Tree (98)

### Graph General
- Number of Islands (200)
- Surrounded Regions (130)
- Clone Graph (133)
- Evaluate Division (399)
- Course Schedule (207)
- Course Schedule II (210)

### Graph BFS
- Snakes and Ladders (909)
- Minimum Genetic Mutation (433)
- Word Ladder (127)

### Trie
- Implement Trie (Prefix Tree) (208)
- Design Add and Search Words Data Structure (211)
- Word Search II (212)

### Backtracking
- Letter Combinations of a Phone Number (17)
- Combinations (77)
- Permutations (46)
- Combination Sum (39)
- N-Queens II (52)
- Generate Parentheses (22)
- Word Search (79)

### Divide & Conquer
- Convert Sorted Array to Binary Search Tree (108)
- Sort List (148)
- Construct Quad Tree (427)
- Merge k Sorted Lists (23)

### Kadane's Algorithm
- Maximum Subarray (53)
- Maximum Sum Circular Subarray (918)

### Binary Search
- Search Insert Position (35)
- Search a 2D Matrix (74)
- Find Peak Element (162)
- Search in Rotated Sorted Array (33)
- Find First and Last Position of Element in Sorted Array (34)
- Find Minimum in Rotated Sorted Array (153)
- Median of Two Sorted Arrays (4)

### Heap
- Kth Largest Element in an Array (215)
- IPO (502)
- Find K Pairs with Smallest Sums (373)
- Find Median from Data Stream (295)

### Bit Manipulation
- Add Binary (67)
- Reverse Bits (190)
- Number of 1 Bits (191)
- Single Number (136)
- Single Number II (137)
- Bitwise AND of Numbers Range (201)

### Math
- Palindrome Number (9)
- Plus One (66)
- Factorial Trailing Zeroes (172)
- Sqrt(x) (69)
- Pow(x, n) (50)
- Max Points on a Line (149)

### 1D DP
- Climbing Stairs (70)
- House Robber (198)
- Word Break (139)
- Coin Change (322)
- Longest Increasing Subsequence (300)

### Multidimensional DP
- Triangle (120)
- Minimum Path Sum (64)
- Unique Paths II (63)
- Longest Palindromic Substring (5)
- Interleaving String (97)
- Edit Distance (72)
- Best Time to Buy and Sell Stock III (123)
- Best Time to Buy and Sell Stock IV (188)
- Maximal Square (221)

## File Naming Convention

Files are named as: `{problem_number}_{problem_name}.{extension}`

Example: `1_Two_Sum.py`, `2_Add_Two_Numbers.cpp`

## Languages

Solutions are available in:
- Python (.py)
- C++ (.cpp)
- Java (.java)
- JavaScript (.js)

## Usage

Each file contains a complete solution for the corresponding problem. You can run them directly or use them as reference for your interview preparation.
"""
    
    with open("top_interview_150/README.md", "w") as f:
        f.write(readme_content)
    
    print("📝 Created README.md in top_interview_150 folder")

if __name__ == "__main__":
    print("🚀 Starting Top 150 Interview Problems extraction...")
    copy_solutions_to_top_150()
    create_readme()
    print("✅ Extraction complete!") 