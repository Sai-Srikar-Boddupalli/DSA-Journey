"""
Problem: Longest Consecutive Sequence
Difficulty: Medium
Link: https://leetcode.com/problems/longest-consecutive-sequence/

This file documents the progression from a brute-force sorting approach 
to two optimal O(n) solutions using Hash Sets and Hash Maps.
"""
from typing import List

# ================================================================
# APPROACH 1: Initial Thought Process (Sorting)
# ================================================================
# Time Complexity: O(n log n) - due to Python's built-in sort
# Space Complexity: O(1) or O(n) depending on the sorting algorithm under the hood
# Notes: Intuitive, but fails the strict O(n) time constraint and struggles 
# with duplicates and broken sequences.

class SolutionBeginner:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = 1
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                n = n + 1
        return n


# ================================================================
# APPROACH 2: Optimal Senior Solution (Hash Set)
# ================================================================
# Time Complexity: O(n) - each number is visited at most twice
# Space Complexity: O(n) - storing the numbers in a set

class SolutionHashSet:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Only start counting if 'num' is the BEGINNING of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


# ================================================================
# APPROACH 3: Alternative Optimal (Hash Map Boundary Tracking)
# ================================================================
# Time Complexity: O(n)
# Space Complexity: O(n) - storing sequences in a dictionary

class SolutionHashMap:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)  # Remove duplicates first
        table = {}
        maxval = 0
        
        for n in nums:
            # Get the length of the left and right sequences (0 if they don't exist)
            left_length = table.get(n - 1, 0)
            right_length = table.get(n + 1, 0)
            
            # Calculate the length of the new combined sequence
            current_length = left_length + right_length + 1
            
            # Update the absolute boundaries of the new sequence
            table[n - left_length] = current_length
            table[n + right_length] = current_length
            
            # Keep track of the maximum length found
            maxval = max(maxval, current_length)
            
        return maxval


"""
================================================================
📝 LESSONS LEARNED & REFACTORING NOTES
================================================================
1. The Hidden Cost of Sorting:
My initial instinct was to sort the array, which logically groups consecutive 
numbers together. However, sorting algorithms always run in O(n log n) time. 
Since the problem strictly required an O(n) solution, sorting immediately 
violated the performance constraints.

2. Guarding Against Edge Cases:
The initial code failed to account for several critical edge cases:
- Empty Arrays: If `nums` is empty, the original code returns 1, but it should return 0.
- Duplicates: If the array contains duplicates (e.g., [1, 2, 2, 3]), the loop 
  fails to recognize the continuation of the streak. Converting the input to a 
  Set automatically handles this.
- Streak Resets: A variable must be used to track the `longest_streak` seen 
  so far, and the `current_streak` must reset when a sequence breaks.

3. Hash Set for O(1) Lookups (Approach 2):
To eliminate sorting, I needed a way to instantly check if the "next" number 
existed. A Hash Set provides O(1) lookups. By adding a strict `if (num - 1) not in num_set:` 
condition, the inner `while` loop ONLY triggers at the absolute beginning of a sequence. 
This guarantees each number is processed a maximum of twice, keeping time complexity at O(n).

4. Hash Map Boundary Tracking (Approach 3):
This approach tracks the length of sequences using a Dictionary. The core 
realization is that when building a sequence, you only need to update the data 
on the absolute edges (boundaries). Any new number will only ever attach to the 
edges of an existing sequence. 
Example: If bridging a left sequence of length 2 and a right sequence of length 1 
with a new number `n`, the new total length is 4. We instantly update `table[n - 2]` 
and `table[n + 1]` to reflect the new sequence size.
"""
