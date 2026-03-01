"""
Problem: Longest Consecutive Sequence
Difficulty: Medium
Link: https://leetcode.com/problems/longest-consecutive-sequence/

================================================================
APPROACH 1: Initial Thought Process (Sorting)
================================================================
"""
from typing import List

class SolutionBeginner:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = 1
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                n = n + 1
        return n

"""
================================================================
APPROACH 2: Optimized Senior Solution (Hash Set)
================================================================
"""
class Solution:
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

"""
================================================================
📝 LESSONS LEARNED & REFACTORING NOTES
================================================================
1. The Hidden Cost of Sorting:
My initial instinct was to sort the array, which logically groups consecutive 
numbers together. However, built-in sorting algorithms (like Python's Timsort) 
always run in $O(n \log n)$ time. Since the problem strictly required an $O(n)$ 
solution, sorting immediately violated the performance constraints.

2. Edge Cases Are Critical:
The initial code failed to account for several critical edge cases:
- Empty Arrays: If `nums` is empty, the original code returns 1, but it should return 0.
- Duplicates: If the array contains duplicates (e.g., [1, 2, 2, 3]), the `nums[i+1] - nums[i] == 1` 
  condition fails on the duplicate, prematurely breaking the streak count.
- Streak Resets: The original code continuously added to `n` without ever resetting 
  it when a gap in the sequence occurred. 

3. The "Aha!" Moment - Hash Sets for $O(1)$ Lookups:
To eliminate sorting, I needed a way to instantly check if the "next" number 
existed. Converting the list to a Hash Set removes duplicates automatically 
and allows for $O(1)$ (instant) lookups. 

4. Maintaining $O(n)$ Time with a Nested Loop:
At first glance, putting a `while` loop inside a `for` loop looks like it 
would result in $O(n^2)$ time complexity. However, the strict `if (num - 1) not in num_set:` 
condition acts as a gatekeeper. It guarantees the `while` loop ONLY triggers 
if we are at the absolute beginning of a sequence. Because of this, the inner 
loop only ever visits each number a maximum of one time. Therefore, the 
overall time complexity remains strictly $O(n)$.
"""
