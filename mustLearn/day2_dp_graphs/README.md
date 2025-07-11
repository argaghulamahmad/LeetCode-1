# Day 2: Advanced Algorithms - Dynamic Programming & Graphs

## 🎯 Focus Areas
- **Dynamic Programming**: Classic patterns, optimization techniques
- **Graph Algorithms**: DFS/BFS, topological sort, union-find
- **Advanced Problem Solving**: Complex optimization problems

## 📚 Morning Session (4 hours): Dynamic Programming

### 1. Unique Paths (Problem 62)
**Key Concept**: Grid Dynamic Programming
- **Approach**: Fill DP table with path counts
- **Time Complexity**: O(m×n)
- **Space Complexity**: O(m×n) → O(n) optimized
- **Pattern**: Classic grid DP problem
- **Variation**: With obstacles, different directions

### 2. House Robber (Problem 198)
**Key Concept**: Classic Dynamic Programming
- **Approach**: Choose or skip current house
- **Time Complexity**: O(n)
- **Space Complexity**: O(1) optimized
- **Key Insight**: Cannot rob adjacent houses
- **Pattern**: State machine DP

### 3. Longest Increasing Subsequence (Problem 300)
**Key Concept**: DP with Binary Search
- **Approach**: Maintain increasing sequence with binary search
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)
- **Advanced**: Patience sorting algorithm
- **Variation**: Can find actual sequence too

### 4. Coin Change (Problem 322)
**Key Concept**: Unbounded Knapsack
- **Approach**: Try all coin denominations
- **Time Complexity**: O(amount × coins)
- **Space Complexity**: O(amount)
- **Edge Cases**: Impossible to make amount
- **Pattern**: Classic unbounded knapsack

### 5. Word Break (Problem 139)
**Key Concept**: String Dynamic Programming
- **Approach**: Check if substring can be broken
- **Time Complexity**: O(n³) with optimization
- **Space Complexity**: O(n)
- **Key Insight**: Use DP to avoid recomputation
- **Variation**: Return all possible breaks

## 📚 Afternoon Session (4 hours): Graph Algorithms

### 6. Word Ladder (Problem 127)
**Key Concept**: BFS with Optimization
- **Approach**: BFS with word transformation
- **Time Complexity**: O(26 × word_length × word_list)
- **Space Complexity**: O(word_list)
- **Optimization**: Two-way BFS, preprocessing
- **Pattern**: Shortest path in word graph

### 7. Clone Graph (Problem 133)
**Key Concept**: Graph Traversal
- **Approach**: DFS/BFS with hash map
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)
- **Key Insight**: Map old nodes to new nodes
- **Pattern**: Graph copying with cycle detection

### 8. Number of Islands (Problem 200)
**Key Concept**: DFS/BFS on Grid
- **Approach**: Flood fill connected components
- **Time Complexity**: O(m×n)
- **Space Complexity**: O(m×n) worst case
- **Variations**: Count islands, largest island
- **Pattern**: Connected components in grid

### 9. Course Schedule (Problem 207)
**Key Concept**: Topological Sort
- **Approach**: Detect cycles in directed graph
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V + E)
- **Key Insight**: Use DFS or Kahn's algorithm
- **Pattern**: Cycle detection in DAG

### 10. Redundant Connection (Problem 684)
**Key Concept**: Union-Find
- **Approach**: Detect cycle in undirected graph
- **Time Complexity**: O(n log n) with path compression
- **Space Complexity**: O(n)
- **Key Insight**: Union-Find for cycle detection
- **Pattern**: Minimum spanning tree variation

## 🎯 Key Learning Objectives for Day 2

### Dynamic Programming Mastery
- ✅ Grid DP patterns
- ✅ State machine DP
- ✅ Optimization techniques (space/time)
- ✅ Unbounded knapsack problems
- ✅ String DP problems

### Graph Algorithm Mastery
- ✅ DFS/BFS implementations
- ✅ Topological sorting
- ✅ Union-Find data structure
- ✅ Cycle detection
- ✅ Connected components

### Advanced Problem Solving
- ✅ Complex optimization
- ✅ Multiple algorithm approaches
- ✅ Trade-off analysis
- ✅ Edge case handling

## 📝 Practice Strategy for Day 2

### For Each DP Problem:
1. **Identify the subproblem** structure
2. **Write the recurrence** relation
3. **Choose the DP table** structure
4. **Implement bottom-up** or top-down
5. **Optimize space** if possible

### For Each Graph Problem:
1. **Model the problem** as a graph
2. **Choose appropriate** traversal (DFS/BFS)
3. **Handle cycles** and visited states
4. **Optimize for** specific constraints
5. **Consider multiple** approaches

### Evening Review:
- [ ] Review all 10 problems
- [ ] Identify DP patterns and variations
- [ ] Practice graph modeling
- [ ] Note optimization techniques
- [ ] Prepare for Day 3

## 🚀 Success Checklist for Day 2

By the end of Day 2, you should be able to:
- ✅ Solve grid DP problems efficiently
- ✅ Implement classic DP patterns
- ✅ Model problems as graphs
- ✅ Apply appropriate graph algorithms
- ✅ Optimize solutions for time/space

## 🔧 Advanced Techniques to Master

### Dynamic Programming
- **State Compression**: Reduce space complexity
- **Memoization**: Top-down approach
- **Tabulation**: Bottom-up approach
- **Space Optimization**: Use rolling arrays

### Graph Algorithms
- **Two-way BFS**: Optimize shortest path
- **Union-Find**: Cycle detection and MST
- **Topological Sort**: Dependency resolution
- **Connected Components**: Flood fill algorithms

**Remember**: Focus on understanding when to use each technique and how to optimize! 