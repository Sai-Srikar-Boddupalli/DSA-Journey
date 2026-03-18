"""
Problem: Concatenation of Array
Difficulty: Easy
Link: https://leetcode.com/problems/concatenation-of-array/

This file documents the progression from intuitive looping to manual 
memory allocation, and finally to a highly optimized Pythonic one-liner.
"""
from typing import List

# ================================================================
# APPROACH 1: Iteration with Append (The Intuitive Approach)
# ================================================================
# Time Complexity: O(n) - visiting each element twice
# Space Complexity: O(n) - creating a new array
# Notes: A very readable and logical approach. However, using .append() 
# inside a loop forces Python to dynamically resize the array in memory 
# under the hood, which is slightly less efficient than pre-allocating.

class SolutionBeginner:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        # First pass
        for i in nums:
            ans.append(i)
        # Second pass
        for i in nums:
            ans.append(i)
        return ans


# ================================================================
# APPROACH 2: Manual Index Math (The "Under the Hood" Approach)
# ================================================================
# Time Complexity: O(n) - we iterate through the original list once
# Space Complexity: O(n) - creating a new array of size 2n
# Notes: If asked to solve this without Python's built-in concatenation, 
# we manually allocate the space upfront to avoid resizing delays, and 
# use index math to place elements in both halves simultaneously.

class SolutionManual:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Pre-allocate an array of size 2n with zeros
        ans = [0] * (2 * n)
        
        for i in range(n):
            ans[i] = nums[i]          # Place in the first half
            ans[i + n] = nums[i]      # Place in the second half
            
        return ans


# ================================================================
# APPROACH 3: Optimal Senior Solution (Pythonic Concatenation)
# ================================================================
# Time Complexity: O(n) - C-level optimized memory copy
# Space Complexity: O(n) - returning a new list of size 2n
# Notes: This is the most readable and Pythonic way to solve the problem 
# in production. The `+` operator for lists is heavily optimized.

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


"""
================================================================
📝 LESSONS LEARNED & REFACTORING NOTES
================================================================
1. The Hidden Cost of Dynamic Arrays (.append):
While `ans.append(i)` is highly readable, it forces the system to continually 
check if the array has enough memory, and reallocate memory when it runs out. 
This is fine for small scripts, but inefficient at scale.

2. Pre-allocating Memory (Approach 2):
When building arrays manually, it is computationally faster to pre-allocate 
the exact size you need upfront (e.g., `ans = [0] * (2*n)`). This completely 
eliminates the overhead of dynamic memory resizing.

3. Language Fluency vs. Algorithmic Knowledge:
Using `nums + nums` is the absolute best way to write this in a production 
environment. However, relying solely on language-specific syntactic sugar 
can be a trap in technical interviews. It is critical to also know how to 
manipulate the underlying memory and indices manually.
"""
