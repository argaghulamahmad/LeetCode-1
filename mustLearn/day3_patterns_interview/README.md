# Day 3: Problem-Solving Patterns & Interview Skills

## 🎯 Focus Areas
- **Advanced Patterns**: Sliding window, two pointers, binary search variations
- **Interview Skills**: Communication, optimization, edge case handling
- **Mock Interview Practice**: Real interview simulation

## 📚 Morning Session (4 hours): Advanced Patterns

### 1. Longest Substring Without Repeating Characters (Problem 3)
**Key Concept**: Sliding Window
- **Approach**: Expand window until duplicate, then contract
- **Time Complexity**: O(n)
- **Space Complexity**: O(min(m, n)) - character set size
- **Key Insight**: Use hash set to track characters in window
- **Pattern**: Classic sliding window problem

### 2. Container With Most Water (Problem 11)
**Key Concept**: Two Pointers
- **Approach**: Start from ends, move pointer with smaller height
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Key Insight**: Greedy approach - always move smaller pointer
- **Pattern**: Two pointers from opposite ends

### 3. 3Sum (Problem 15)
**Key Concept**: Two Pointers with Sorting
- **Approach**: Sort + two pointers for each first element
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1) excluding output
- **Key Insight**: Avoid duplicates by skipping same values
- **Pattern**: Three pointers with sorting

### 4. Search in Rotated Sorted Array (Problem 33)
**Key Concept**: Binary Search Variation
- **Approach**: Modified binary search for rotated array
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
- **Key Insight**: One half is always sorted
- **Pattern**: Binary search with conditions

### 5. Subsets (Problem 78)
**Key Concept**: Backtracking
- **Approach**: Generate all combinations using backtracking
- **Time Complexity**: O(2ⁿ)
- **Space Complexity**: O(n) for recursion stack
- **Key Insight**: Include/exclude each element
- **Pattern**: Classic backtracking problem

### 6. Top K Frequent Elements (Problem 347)
**Key Concept**: Heap (Priority Queue)
- **Approach**: Count frequencies, use min-heap for top K
- **Time Complexity**: O(n log k)
- **Space Complexity**: O(n)
- **Key Insight**: Use heap to maintain top K elements
- **Pattern**: Heap for top K problems

## 📚 Afternoon Session (4 hours): Mock Interview Practice

### 7. Add Two Numbers (Problem 2)
**Key Concept**: Linked List Manipulation
- **Approach**: Add digits with carry, handle different lengths
- **Time Complexity**: O(max(m, n))
- **Space Complexity**: O(max(m, n))
- **Interview Tip**: Handle carry and different list lengths
- **Pattern**: Linked list arithmetic

### 8. Longest Palindromic Substring (Problem 5)
**Key Concept**: Expand Around Center
- **Approach**: Try each position as center, expand outward
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)
- **Key Insight**: Handle odd and even length palindromes
- **Pattern**: Center expansion technique

### 9. Valid Anagram (Problem 242)
**Key Concept**: Hash Table
- **Approach**: Count character frequencies
- **Time Complexity**: O(n)
- **Space Complexity**: O(1) - fixed character set
- **Edge Cases**: Different lengths, empty strings
- **Pattern**: Character counting

### 10. Missing Number (Problem 268)
**Key Concept**: Math/Bit Manipulation
- **Approach**: Use sum formula or XOR
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Key Insight**: Sum of 0 to n minus array sum
- **Pattern**: Mathematical approach

### 11. Move Zeroes (Problem 283)
**Key Concept**: Two Pointers
- **Approach**: Move non-zero elements to front
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Key Insight**: In-place modification
- **Pattern**: Two pointers for array manipulation

## 🎯 Interview Skills to Master

### Communication Skills
- ✅ **Clarify the problem**: Ask about constraints, edge cases
- ✅ **Think out loud**: Explain your thought process
- ✅ **Start simple**: Begin with brute force approach
- ✅ **Optimize step by step**: Show improvement process
- ✅ **Test your code**: Walk through examples

### Problem-Solving Approach
- ✅ **Pattern recognition**: Identify common algorithms
- ✅ **Multiple approaches**: Consider different solutions
- ✅ **Trade-off analysis**: Time vs space complexity
- ✅ **Edge case handling**: Empty inputs, single elements
- ✅ **Optimization**: Improve efficiency when possible

### Mock Interview Practice
- ✅ **Time management**: 15-20 min for easy, 25-30 min for medium
- ✅ **Code quality**: Clean, readable, well-commented
- ✅ **Error handling**: Consider edge cases
- ✅ **Follow-up questions**: Be ready for variations

## 📝 Practice Strategy for Day 3

### Morning Pattern Practice:
1. **Identify the pattern** quickly
2. **Implement efficiently** with proper data structures
3. **Optimize immediately** if possible
4. **Handle edge cases** systematically
5. **Explain trade-offs** clearly

### Afternoon Mock Interviews:
1. **Clarify requirements** first
2. **Start with examples** and simple cases
3. **Implement step by step** with explanation
4. **Test with edge cases** and examples
5. **Discuss optimizations** and alternatives

### Evening Review:
- [ ] Review all 11 problems
- [ ] Practice explaining solutions
- [ ] Identify areas for improvement
- [ ] Prepare for actual interview
- [ ] Review common patterns

## 🚀 Success Checklist for Day 3

By the end of Day 3, you should be able to:
- ✅ Recognize and implement advanced patterns quickly
- ✅ Communicate solutions clearly and concisely
- ✅ Handle edge cases and optimizations
- ✅ Manage interview time effectively
- ✅ Demonstrate problem-solving confidence

## 🔧 Advanced Patterns to Master

### Sliding Window
- **Fixed size**: Count occurrences
- **Variable size**: Longest/shortest substring
- **Optimization**: Two pointers technique

### Two Pointers
- **Same direction**: Remove duplicates, move zeroes
- **Opposite direction**: Container with most water
- **Multiple pointers**: 3Sum, 4Sum

### Binary Search Variations
- **Standard**: Find target in sorted array
- **Rotated array**: Modified conditions
- **Answer space**: Binary search on result

### Backtracking
- **Subsets**: Include/exclude elements
- **Permutations**: Generate all arrangements
- **Combinations**: Generate all combinations

## 💡 Interview Pro Tips

### Before Starting:
- Ask clarifying questions about input/output
- Consider edge cases and constraints
- Plan your approach before coding

### During Implementation:
- Write clean, readable code
- Add comments for complex logic
- Test with simple examples

### After Solution:
- Discuss time/space complexity
- Mention possible optimizations
- Ask about follow-up questions

**Remember**: Confidence comes from practice and preparation! 