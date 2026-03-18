"""
Problem: Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

This file documents the complete progression of solving Two Sum: starting from 
flawed initial logic, correcting it to a working brute-force solution, and 
finally optimizing it to an O(n) One-Pass Hash Map.
"""
from typing import List

# ================================================================
# APPROACH 0.1: Flawed Initial Attempt (The Adjacent Trap)
# ================================================================
# Notes: My very first instinct was to loop through and check neighbors.
# Fails because it ONLY checks numbers right next to each other. 
# It also causes an IndexError when `i` reaches the end of the list.

class SolutionAttemptOne:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            # BUG: IndexError at the end of the loop, and misses non-adjacent pairs
            if nums[i] + nums[i+1] == target:
                return [i, i+1]


# ================================================================
# APPROACH 0.2: Flawed Second Attempt (The Self-Matching Trap)
# ================================================================
# Notes: I realized I needed a nested loop to check all combinations.
# Fails because the inner loop always starts at 1, meaning it will 
# eventually check a number against itself (e.g., nums[1] + nums[1]), 
# which violates the rule: "you may not use the same element twice."

class SolutionAttemptTwo:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                # BUG: i and j can equal the same index, using the same element twice
                if nums[i] + nums[j] == target:
                    return [i, j]


# ================================================================
# APPROACH 1: Working Brute Force (Nested Loops)
# ================================================================
# Time Complexity: O(n^2) - checking every possible valid pair
# Space Complexity: O(1) - no extra memory used
# Notes: Corrected the nested loop by ensuring `j` always starts at `i + 1`. 
# This perfectly avoids self-matching, but is too slow for massive inputs.

class SolutionBruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            # FIX: Start j exactly one index AFTER i 
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# ================================================================
# APPROACH 2: Optimal Senior Solution (One-Pass Hash Map)
# ================================================================
# Time Complexity: O(n) - we traverse the list exactly once
# Space Complexity: O(n) - storing numbers and indices in a dictionary
# Notes: Traded space for time. By tracking what we've seen in a Hash Map,
# we instantly know if the complement exists.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to map: array_value -> array_index
        prev_map = {}  

        for i, num in enumerate(nums):
            # What number do we need to reach the target?
            complement = target - num

            # Have we seen that number before?
            if complement in prev_map:
                # If yes, return the index of the stored complement, and our current index
                return [prev_map[complement], i]
            
            # If not, store the current number and its index in the map
            prev_map[num] = i


"""
================================================================
📝 LESSONS LEARNED & REFACTORING NOTES
================================================================
1. The Danger of Index Out of Bounds:
My first attempt tried to look ahead using `nums[i+1]`. I learned that if you 
do this inside a standard loop, the final iteration will always crash because 
it tries to access an index that doesn't exist.

2. Avoiding Self-Matching:
When setting up a brute-force nested loop, the inner loop variable `j` must 
depend on the outer loop variable `i`. Starting `j` at a static number like `1` 
guarantees you will accidentally evaluate an element against itself.

3. The Time vs. Space Trade-off:
The brute-force solution is highly memory efficient (Space: O(1)), but scales terribly 
with large inputs (Time: O(n^2)). In modern software engineering, we frequently 
trade memory (Space) to buy speed (Time).

4. The "Complement" Concept with Hash Maps:
To achieve O(n) time, we utilize a Hash Map (Python Dictionary). By calculating 
the "complement" (target - current_number) at each step, we can use the O(1) 
lookup time of the dictionary to instantly check if we have already passed the 
number we need.
"""
