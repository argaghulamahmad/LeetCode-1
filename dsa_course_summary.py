#!/usr/bin/env python3
"""
Script to generate a summary of the Data Structures and Algorithms course extraction results.
"""

import os
import re
from collections import defaultdict

# Data Structures and Algorithms Course Problems (same as in extract_dsa_course.py)
DSA_COURSE_PROBLEMS = [
    # Arrays and Strings
    "1. Two Sum",
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

def analyze_dsa_course():
    """Analyze the data_structures_algorithms_course folder and generate statistics."""
    folder_path = "data_structures_algorithms_course"
    
    if not os.path.exists(folder_path):
        print(f"❌ Folder '{folder_path}' not found!")
        return
    
    # Get all files in the folder
    files = os.listdir(folder_path)
    solution_files = [f for f in files if f.endswith(('.py', '.cpp', '.java', '.js'))]
    
    # Extract problem numbers from filenames
    found_problems = set()
    language_stats = defaultdict(int)
    
    for file in solution_files:
        # Extract problem number from filename (e.g., "3_Longest_Substring_Without_Repeating_Characters.py")
        match = re.match(r'(\d+)_', file)
        if match:
            problem_num = int(match.group(1))
            found_problems.add(problem_num)
        
        # Count languages
        ext = os.path.splitext(file)[1]
        language_stats[ext] += 1
    
    # Check which problems from DSA_COURSE_PROBLEMS are found
    found_in_course = []
    missing_from_course = []
    
    for problem in DSA_COURSE_PROBLEMS:
        problem_num = extract_problem_number(problem)
        if problem_num:
            if problem_num in found_problems:
                found_in_course.append(problem)
            else:
                missing_from_course.append(problem)
    
    # Generate report
    print("📊 Data Structures and Algorithms Course - Analysis Report")
    print("=" * 70)
    print(f"📁 Total files in folder: {len(files)}")
    print(f"💻 Solution files: {len(solution_files)}")
    print(f"✅ Problems found: {len(found_in_course)}")
    print(f"❌ Problems missing: {len(missing_from_course)}")
    print(f"📈 Coverage: {len(found_in_course)}/{len(DSA_COURSE_PROBLEMS)} ({len(found_in_course)/len(DSA_COURSE_PROBLEMS)*100:.1f}%)")
    
    print("\n🔤 Language Distribution:")
    for lang, count in sorted(language_stats.items()):
        print(f"   {lang}: {count} files")
    
    # Category analysis
    categories = {
        "Arrays and Strings": ["1. Two Sum", "88. Merge Sorted Array", "27. Remove Element", "26. Remove Duplicates from Sorted Array", "80. Remove Duplicates from Sorted Array II", "169. Majority Element", "189. Rotate Array", "121. Best Time to Buy and Sell Stock", "122. Best Time to Buy and Sell Stock II", "55. Jump Game", "45. Jump Game II", "274. H-Index", "380. Insert Delete GetRandom O(1)", "238. Product of Array Except Self", "134. Gas Station", "135. Candy", "42. Trapping Rain Water", "13. Roman to Integer", "12. Integer to Roman", "58. Length of Last Word", "14. Longest Common Prefix", "151. Reverse Words in a String", "6. ZigZag Conversion", "28. Find the Index of the First Occurrence in a String", "68. Text Justification"],
        "Two Pointers": ["125. Valid Palindrome", "392. Is Subsequence", "167. Two Sum II - Input Array Is Sorted", "11. Container With Most Water", "15. 3Sum"],
        "Sliding Window": ["209. Minimum Size Subarray Sum", "3. Longest Substring Without Repeating Characters", "30. Substring with Concatenation of All Words", "76. Minimum Window Substring"],
        "Matrix": ["36. Valid Sudoku", "54. Spiral Matrix", "48. Rotate Image", "73. Set Matrix Zeroes", "289. Game of Life"],
        "Hashmap": ["383. Ransom Note", "205. Isomorphic Strings", "290. Word Pattern", "242. Valid Anagram", "49. Group Anagrams", "202. Happy Number", "219. Contains Duplicate II", "128. Longest Consecutive Sequence"],
        "Intervals": ["228. Summary Ranges", "56. Merge Intervals", "57. Insert Interval", "452. Minimum Number of Arrows to Burst Balloons"],
        "Stack": ["20. Valid Parentheses", "71. Simplify Path", "155. Min Stack", "150. Evaluate Reverse Polish Notation", "224. Basic Calculator"],
        "Linked List": ["141. Linked List Cycle", "2. Add Two Numbers", "21. Merge Two Sorted Lists", "138. Copy List with Random Pointer", "92. Reverse Linked List II", "25. Reverse Nodes in k-Group", "19. Remove Nth Node From End of List", "82. Remove Duplicates from Sorted List II", "61. Rotate List", "86. Partition List", "146. LRU Cache"],
        "Binary Tree General": ["104. Maximum Depth of Binary Tree", "100. Same Tree", "226. Invert Binary Tree", "101. Symmetric Tree", "105. Construct Binary Tree from Preorder and Inorder Traversal", "106. Construct Binary Tree from Inorder and Postorder Traversal", "117. Populating Next Right Pointers in Each Node II", "114. Flatten Binary Tree to Linked List", "112. Path Sum", "129. Sum Root to Leaf Numbers", "124. Binary Tree Maximum Path Sum", "173. Binary Search Tree Iterator", "222. Count Complete Tree Nodes", "236. Lowest Common Ancestor of a Binary Tree"],
        "Binary Tree BFS": ["199. Binary Tree Right Side View", "637. Average of Levels in Binary Tree", "102. Binary Tree Level Order Traversal", "103. Binary Tree Zigzag Level Order Traversal"],
        "Binary Search Tree": ["530. Minimum Absolute Difference in BST", "230. Kth Smallest Element in a BST", "98. Validate Binary Search Tree"],
        "Graph General": ["200. Number of Islands", "130. Surrounded Regions", "133. Clone Graph", "399. Evaluate Division", "207. Course Schedule", "210. Course Schedule II"],
        "Graph BFS": ["909. Snakes and Ladders", "433. Minimum Genetic Mutation", "127. Word Ladder"],
        "Trie": ["208. Implement Trie (Prefix Tree)", "211. Design Add and Search Words Data Structure", "212. Word Search II"],
        "Backtracking": ["17. Letter Combinations of a Phone Number", "77. Combinations", "46. Permutations", "39. Combination Sum", "52. N-Queens II", "22. Generate Parentheses", "79. Word Search"],
        "Divide & Conquer": ["108. Convert Sorted Array to Binary Search Tree", "148. Sort List", "427. Construct Quad Tree", "23. Merge k Sorted Lists"],
        "Kadane's Algorithm": ["53. Maximum Subarray", "918. Maximum Sum Circular Subarray"],
        "Binary Search": ["35. Search Insert Position", "74. Search a 2D Matrix", "162. Find Peak Element", "33. Search in Rotated Sorted Array", "34. Find First and Last Position of Element in Sorted Array", "153. Find Minimum in Rotated Sorted Array", "4. Median of Two Sorted Arrays"],
        "Heap": ["215. Kth Largest Element in an Array", "502. IPO", "373. Find K Pairs with Smallest Sums", "295. Find Median from Data Stream"],
        "Bit Manipulation": ["67. Add Binary", "190. Reverse Bits", "191. Number of 1 Bits", "136. Single Number", "137. Single Number II", "201. Bitwise AND of Numbers Range"],
        "Math": ["9. Palindrome Number", "66. Plus One", "172. Factorial Trailing Zeroes", "69. Sqrt(x)", "50. Pow(x, n)", "149. Max Points on a Line"],
        "1D DP": ["70. Climbing Stairs", "198. House Robber", "139. Word Break", "322. Coin Change", "300. Longest Increasing Subsequence"],
        "Multidimensional DP": ["120. Triangle", "64. Minimum Path Sum", "63. Unique Paths II", "5. Longest Palindromic Substring", "97. Interleaving String", "72. Edit Distance", "123. Best Time to Buy and Sell Stock III", "188. Best Time to Buy and Sell Stock IV", "221. Maximal Square"]
    }
    
    print(f"\n📚 Category Coverage:")
    for category, problems in categories.items():
        found_count = sum(1 for p in problems if extract_problem_number(p) in found_problems)
        total_count = len(problems)
        percentage = (found_count / total_count) * 100 if total_count > 0 else 0
        print(f"   {category}: {found_count}/{total_count} ({percentage:.1f}%)")
    
    print(f"\n✅ Found Problems ({len(found_in_course)}):")
    for problem in sorted(found_in_course, key=lambda x: extract_problem_number(x)):
        print(f"   ✓ {problem}")
    
    print(f"\n❌ Missing Problems ({len(missing_from_course)}):")
    for problem in sorted(missing_from_course, key=lambda x: extract_problem_number(x)):
        print(f"   ✗ {problem}")
    
    # Save detailed report to file
    with open("data_structures_algorithms_course/COURSE_ANALYSIS.md", "w") as f:
        f.write("# Data Structures and Algorithms Course - Analysis Report\n\n")
        f.write(f"## Summary\n")
        f.write(f"- Total files: {len(files)}\n")
        f.write(f"- Solution files: {len(solution_files)}\n")
        f.write(f"- Problems found: {len(found_in_course)}\n")
        f.write(f"- Problems missing: {len(missing_from_course)}\n")
        f.write(f"- Coverage: {len(found_in_course)}/{len(DSA_COURSE_PROBLEMS)} ({len(found_in_course)/len(DSA_COURSE_PROBLEMS)*100:.1f}%)\n\n")
        
        f.write("## Language Distribution\n")
        for lang, count in sorted(language_stats.items()):
            f.write(f"- {lang}: {count} files\n")
        
        f.write("\n## Category Coverage\n")
        for category, problems in categories.items():
            found_count = sum(1 for p in problems if extract_problem_number(p) in found_problems)
            total_count = len(problems)
            percentage = (found_count / total_count) * 100 if total_count > 0 else 0
            f.write(f"- {category}: {found_count}/{total_count} ({percentage:.1f}%)\n")
        
        f.write("\n## Found Problems\n")
        for problem in sorted(found_in_course, key=lambda x: extract_problem_number(x)):
            f.write(f"- ✓ {problem}\n")
        
        f.write("\n## Missing Problems\n")
        for problem in sorted(missing_from_course, key=lambda x: extract_problem_number(x)):
            f.write(f"- ✗ {problem}\n")
    
    print(f"\n📝 Detailed report saved to: data_structures_algorithms_course/COURSE_ANALYSIS.md")

if __name__ == "__main__":
    analyze_dsa_course()